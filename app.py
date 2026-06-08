import streamlit as st
import pandas as pd
import networkx as nx
import numpy as np
import os
import math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

from core.skill_graph import (
    build_curriculum_graph,
    calculate_pagerank,
    get_focused_prerequisite_graph,
    calculate_review_recommendations,
)
from core.mastery_model import (
    apply_practice_result,
    get_prerequisite_factor,
    effective_learning_rate,
)
from core.prediction import find_sessions_to_target, linear_regression_prediction
from core.tasks import load_tasks, check_answer
from core.generated_tasks import generated_task_for_skill
from core.navigation import (
    build_learning_route,
    choose_next_after_attempt,
)
from components.cytoscape_graph import render_cytoscape_graph
from core.profiles import load_profile, PROFILE_META
from core.recommendations import recommend_related_skills


# ── CONFIG ────────────────────────────────────────────────────────────────────

st.set_page_config(page_title="SkillGraph Tutor", layout="wide", page_icon="🧠")


# ── CSS ───────────────────────────────────────────────────────────────────────

st.markdown(
    """
    <style>
    /* ── Design tokens ──────────────────────────────────────────────── */
    :root {
        --bg:          #000000;
        --bg-panel:    #070A12;
        --bg-panel-2:  #0B1020;
        --border:      rgba(234,239,247,0.10);
        --border-soft: rgba(234,239,247,0.06);
        --text-1:      #EAEFF7;
        --text-2:      #9AA4B2;
        --text-3:      #6B7280;
        --accent:      #00E5FF;
        --accent-soft: #7CFFB2;
        --warn:        #FF6B6B;
        --dev:         #F6D06F;
        --strong:      #8DE4AF;
    }

    /* ── Page background ────────────────────────────────────────────── */
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    .main { background: #000000 !important; }

    .main .block-container {
        max-width: 1640px;
        padding-top: 0.75rem;
        background: transparent !important;
    }

    [data-testid="stHeader"] { background: transparent !important; }

    /* ── Sidebar ────────────────────────────────────────────────────── */
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div:first-child {
        background: #070A12 !important;
        border-right: 1px solid rgba(234,239,247,0.07) !important;
    }
    [data-testid="stSidebarContent"] { background: transparent !important; }

    /* ── Streamlit widgets: inputs, selects ─────────────────────────── */
    [data-testid="stTextInput"] input,
    [data-testid="stTextInput"] textarea {
        background: #0B1020 !important;
        border: 1px solid rgba(234,239,247,0.12) !important;
        border-radius: 10px !important;
        color: #EAEFF7 !important;
        font-size: 0.95rem !important;
    }
    [data-testid="stTextInput"] input:focus {
        border-color: #00E5FF !important;
        box-shadow: 0 0 0 2px rgba(0,229,255,0.15) !important;
    }
    [data-baseweb="select"] > div {
        background: #0B1020 !important;
        border: 1px solid rgba(234,239,247,0.12) !important;
        border-radius: 10px !important;
        color: #EAEFF7 !important;
    }
    [data-baseweb="popover"] { background: #0B1020 !important; }
    [data-baseweb="menu"]    { background: #0B1020 !important; border: 1px solid rgba(234,239,247,0.12) !important; }
    [data-baseweb="option"]  { background: #0B1020 !important; color: #EAEFF7 !important; }
    [data-baseweb="option"]:hover { background: #121828 !important; }

    /* ── Expanders ──────────────────────────────────────────────────── */
    [data-testid="stExpander"] {
        background: #070A12 !important;
        border: 1px solid rgba(234,239,247,0.08) !important;
        border-radius: 12px !important;
    }
    [data-testid="stExpanderToggleIcon"] { color: #9AA4B2 !important; }

    /* ── Streamlit default dividers ─────────────────────────────────── */
    hr { border-color: rgba(234,239,247,0.08) !important; }

    /* ── Buttons ────────────────────────────────────────────────────── */
    div.stButton > button {
        min-height: 2.6rem;
        font-size: 0.92rem;
        font-weight: 700;
        border-radius: 11px;
        border: 1px solid rgba(234,239,247,0.13);
        background: #0B1020;
        color: #EAEFF7;
        transition: border-color 0.18s, box-shadow 0.18s, color 0.18s;
    }
    div.stButton > button:hover {
        border-color: #00E5FF !important;
        box-shadow: 0 0 0 1px rgba(0,229,255,0.25) !important;
        color: #00E5FF !important;
        background: #0B1020 !important;
    }
    div.stButton > button[kind="primary"],
    div.stButton > button[data-testid="baseButton-primary"] {
        background: linear-gradient(135deg, #00E5FF 0%, #7CFFB2 100%) !important;
        color: #000000 !important;
        border: none !important;
        font-weight: 800 !important;
    }
    div.stButton > button[kind="primary"]:hover {
        opacity: 0.90 !important;
        box-shadow: 0 0 18px rgba(0,229,255,0.30) !important;
    }

    /* ── Progress bar ───────────────────────────────────────────────── */
    [data-testid="stProgressBar"] > div { background: #0B1020 !important; }
    [data-testid="stProgressBar"] > div > div { border-radius: 999px !important; }

    /* ── Graph iframe container ─────────────────────────────────────── */
    iframe {
        border-radius: 20px !important;
        border: 1px solid rgba(234,239,247,0.06) !important;
        background: transparent !important;
    }
    [data-testid="stCustomComponentV1"],
    [data-testid="stCustomComponentV1"] > div {
        background: transparent !important;
    }

    /* ── Stat cards ─────────────────────────────────────────────────── */
    .stat-card {
        background: #070A12;
        border: 1px solid rgba(234,239,247,0.10);
        border-radius: 14px;
        padding: 13px 16px;
    }
    .stat-label {
        font-size: 0.70rem;
        color: #6B7280;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 4px;
    }
    .stat-value {
        font-size: 1.05rem;
        font-weight: 700;
        color: #EAEFF7;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    /* ── Route pills ────────────────────────────────────────────────── */
    .route-pill {
        display: inline-block;
        padding: 3px 11px;
        margin: 2px 2px;
        border-radius: 999px;
        background: #0B1020;
        border: 1px solid rgba(234,239,247,0.10);
        color: #6B7280;
        font-size: 0.78rem;
        font-weight: 600;
    }
    .route-pill.active {
        background: rgba(0,229,255,0.08);
        border-color: #00E5FF;
        color: #00E5FF;
    }
    .route-pill.done {
        background: rgba(124,255,178,0.07);
        border-color: rgba(124,255,178,0.35);
        color: #7CFFB2;
    }
    .route-pill.target {
        background: rgba(0,229,255,0.10);
        border-color: #00E5FF;
        color: #00E5FF;
        font-weight: 800;
    }

    /* ── Feedback boxes ─────────────────────────────────────────────── */
    .fb-correct {
        background: rgba(141,228,175,0.07);
        border: 1.5px solid rgba(141,228,175,0.35);
        border-radius: 12px; padding: 11px 15px;
        color: #8DE4AF; font-weight: 600; margin: 8px 0;
    }
    .fb-wrong {
        background: rgba(255,107,107,0.07);
        border: 1.5px solid rgba(255,107,107,0.32);
        border-radius: 12px; padding: 11px 15px;
        color: #FF6B6B; font-weight: 600; margin: 8px 0;
    }
    .fb-idk {
        background: rgba(246,208,111,0.07);
        border: 1.5px solid rgba(246,208,111,0.28);
        border-radius: 12px; padding: 11px 15px;
        color: #F6D06F; font-weight: 600; margin: 8px 0;
    }
    .fb-partial {
        background: rgba(255,184,107,0.07);
        border: 1.5px solid rgba(255,184,107,0.28);
        border-radius: 12px; padding: 11px 15px;
        color: #FFB86B; font-weight: 600; margin: 8px 0;
    }

    /* ── Demo bar ───────────────────────────────────────────────────── */
    .demo-bar {
        background: #070A12;
        border: 1px solid rgba(234,239,247,0.07);
        border-radius: 12px;
        padding: 10px 14px;
        margin-top: 12px;
    }
    .demo-label {
        font-size: 0.67rem;
        color: #6B7280;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    /* ── Task panel card ────────────────────────────────────────────── */
    .task-header {
        background: #070A12;
        border: 1px solid rgba(234,239,247,0.10);
        border-radius: 16px;
        padding: 14px 18px 10px;
        margin-bottom: 12px;
    }
    .task-skill-name {
        font-size: 1.15rem;
        font-weight: 800;
        color: #EAEFF7;
        margin-bottom: 2px;
    }
    .task-area-pill {
        display: inline-block;
        padding: 2px 9px;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 600;
        background: rgba(125,211,252,0.12);
        color: #7DD3FC;
        margin-top: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ── DATA ──────────────────────────────────────────────────────────────────────

@st.cache_data
def load_all_data():
    nodes = pd.read_csv(
        os.path.join(SCRIPT_DIR, "Graph data", "math_algebra_to_university_skill_nodes.csv")
    )
    graph_csv = pd.read_csv(
        os.path.join(SCRIPT_DIR, "Graph data", "math_algebra_to_university_skill_graph.csv")
    )
    tasks = load_tasks(os.path.join(SCRIPT_DIR, "data", "tasks.csv"))

    def clean(v, fallback):
        if v is None or (isinstance(v, float) and np.isnan(v)):
            return fallback
        s = str(v).strip()
        return fallback if s in ("", "nan") else s

    nodes["title"] = nodes.apply(lambda r: clean(r.get("title"), r.get("node_id")), axis=1)
    nodes["area"] = nodes.apply(
        lambda r: clean(r.get("area"), clean(r.get("level_band"), "Other")), axis=1
    )
    return nodes, graph_csv, tasks


nodes_df, graph_df, tasks_data = load_all_data()


# ── SESSION STATE ─────────────────────────────────────────────────────────────

def _init_mastery():
    return {
        row["node_id"]: (0.2 if row.get("node_type") == "atomic_skill" else 0.5)
        for _, row in nodes_df.iterrows()
    }


_DEFAULTS = {
    "screen": "learn",
    "target_skill": None,
    "active_skill": None,
    "learning_route": [],
    "practice_log": [],
    "task_counter": 0,
    "last_feedback": None,
    "show_hint": False,
    "show_answer": False,
    "graph_selected": None,
    "_graph_click_absorbed": None,  # last clicked_id consumed by Python; prevents stale re-fires
    "graph_fullscreen": False,
    "active_profile": "default",
    "consecutive_wrong": {},  # skill_id → count of consecutive Wrong/IDK
}

for _k, _v in _DEFAULTS.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v

if not st.session_state.get("mastery"):
    _m, _log = load_profile(st.session_state.active_profile, nodes_df)
    st.session_state.mastery = _m
    if not st.session_state.practice_log:
        st.session_state.practice_log = _log


# ── CONSTANTS ─────────────────────────────────────────────────────────────────

BASE_LR = 0.30
DIFFICULTY = 1.0
TARGET_MASTERY = 0.8
MINS_PER_ATTEMPT = 12
LEARNING_GAIN = 0.12
PREREQ_GAIN = 0.04
MASTERY_THRESHOLD = 0.6


# ── SIDEBAR: student profile selector ────────────────────────────────────────

_PROFILE_KEYS = ["default", "alina", "artem", "ilya"]

with st.sidebar:
    st.markdown("### 👤 Student Profile")
    _selected_profile = st.radio(
        "Profile",
        _PROFILE_KEYS,
        format_func=lambda k: f"{PROFILE_META[k]['emoji']} {PROFILE_META[k]['name']}",
        index=_PROFILE_KEYS.index(st.session_state.active_profile),
        key="profile_radio",
    )
    meta = PROFILE_META[_selected_profile]
    st.caption(meta["desc"])

    if _selected_profile != st.session_state.active_profile:
        _m, _log = load_profile(_selected_profile, nodes_df)
        st.session_state.mastery = _m
        st.session_state.practice_log = _log
        st.session_state.active_profile = _selected_profile
        for _k in ("target_skill", "active_skill", "last_feedback", "graph_selected",
                   "spring_layout_pos", "consecutive_wrong", "_graph_click_absorbed"):
            st.session_state.pop(_k, None)
        st.session_state.learning_route = []
        st.session_state.task_counter = 0
        st.session_state.show_hint = False
        st.session_state.show_answer = False
        st.rerun()

    st.divider()
    n_practiced = len({e["skill_id"] for e in st.session_state.practice_log})
    n_sessions  = len(st.session_state.practice_log)
    st.metric("Skills practiced", n_practiced)
    st.metric("Total sessions", n_sessions)


# ── GRAPH (rebuilt each run from current mastery) ─────────────────────────────

graph = build_curriculum_graph(nodes_df, graph_df, mastery_dict=st.session_state.mastery)
pagerank_scores = calculate_pagerank(graph, edge_type="prereq")


# ── HELPERS ───────────────────────────────────────────────────────────────────

def fmt_time(minutes: float) -> str:
    m = int(round(minutes))
    h, mins = m // 60, m % 60
    if h == 0:
        return f"{mins} min"
    if mins == 0:
        return f"{h} h"
    return f"{h} h {mins} min"


def resolve_atomic(node_id: str) -> str:
    if node_id not in graph.nodes:
        return node_id
    if graph.nodes[node_id].get("node_type") == "atomic_skill":
        return node_id
    for n in nx.dfs_preorder_nodes(graph, node_id):
        if graph.nodes[n].get("node_type") == "atomic_skill":
            return n
    return node_id


def skill_time_estimate(skill_id: str):
    """Returns (minutes, reachable) using exponential model."""
    if skill_id not in graph.nodes:
        return 40 * MINS_PER_ATTEMPT, False
    mastery_now = graph.nodes[skill_id].get("mastery", 0.2)
    pf = get_prerequisite_factor(graph, skill_id)
    lr = effective_learning_rate(BASE_LR, pf, DIFFICULTY)
    attempts, reachable = find_sessions_to_target(mastery_now, lr, TARGET_MASTERY, max_sessions=40)
    return attempts * MINS_PER_ATTEMPT, reachable


def route_time_estimate(route: list) -> float:
    return sum(
        skill_time_estimate(s)[0]
        for s in route
        if s in graph.nodes and graph.nodes[s].get("mastery", 0) < TARGET_MASTERY
    )


def mastery_history_for(skill_id: str) -> list:
    """Mastery snapshots over time from practice log."""
    history = [e["before"] for e in st.session_state.practice_log if e.get("skill_id") == skill_id]
    if history and skill_id in graph.nodes:
        history.append(graph.nodes[skill_id].get("mastery", 0.2))
    return history


def build_view_graph(target_skill: str):
    """Full atomic-skill graph."""
    atomic = [
        n for n in graph.nodes
        if graph.nodes[n].get("node_type") == "atomic_skill"
    ]
    return graph.subgraph(atomic).copy()


_LAYOUT_VERSION = "v6"  # bump to invalidate cached positions after algorithm changes

def get_spring_positions(subgraph: nx.DiGraph) -> dict:
    """Vogel-spiral (sunflower) layout + spring refinement, cached per session.

    High-PageRank skills are placed near the center of the disk using the
    golden-angle distribution, which fills the canvas uniformly without the
    empty-center problem of plain spring_layout.  50 spring iterations then
    pull connected skills slightly closer together to aid visual clustering.
    """
    if (st.session_state.get("spring_layout_version") == _LAYOUT_VERSION
            and "spring_layout_pos" in st.session_state):
        cached = st.session_state["spring_layout_pos"]
        return {n: cached.get(n, (0.0, 0.0)) for n in subgraph.nodes}

    G = nx.DiGraph()
    for n in subgraph.nodes:
        G.add_node(n)
    for u, v, d in subgraph.edges(data=True):
        if d.get("edge_type") == "prereq":
            G.add_edge(u, v)

    # PageRank on the prereq subgraph to rank importance
    pr = nx.pagerank(G, weight=None) if G.number_of_edges() > 0 else {n: 1.0 for n in G}

    # Vogel spiral: sort by PR descending so high-PR nodes land at center
    sorted_nodes = sorted(G.nodes, key=lambda n: -pr.get(n, 0.0))
    n_nodes = max(len(sorted_nodes), 1)
    golden_angle = math.pi * (3.0 - math.sqrt(5.0))  # ≈ 137.5°
    init_pos: dict = {}
    for i, node in enumerate(sorted_nodes):
        r = math.sqrt((i + 0.5) / n_nodes)   # radius ∈ (0, 1]
        theta = i * golden_angle
        init_pos[node] = (r * math.cos(theta), r * math.sin(theta))

    # Light spring pass to pull connected skills together
    pos = nx.spring_layout(G, pos=init_pos, k=1.0, iterations=50, seed=42, weight=None)

    SCALE = 4500
    scaled = {
        n: (float(x * SCALE), float(-y * SCALE))
        for n, (x, y) in pos.items()
    }
    st.session_state["spring_layout_pos"] = scaled
    st.session_state["spring_layout_version"] = _LAYOUT_VERSION
    return scaled


def area_color(area_name: str) -> str:
    palette = [
        "#6EE7F2",  # cyan
        "#B8A1FF",  # soft purple
        "#8DE4AF",  # mint green
        "#FFB86B",  # warm orange
        "#F6D06F",  # golden yellow
        "#7DD3FC",  # sky blue
        "#C084FC",  # violet
        "#34D399",  # emerald
        "#F472B6",  # rose
        "#60A5FA",  # blue
        "#A78BFA",  # indigo
        "#FB923C",  # amber orange
        "#4ADE80",  # green
        "#E879F9",  # fuchsia
        "#38BDF8",  # light sky
        "#FCA5A5",  # soft coral
    ]
    if not area_name:
        return palette[0]
    digest = sum(ord(ch) for ch in area_name)
    return palette[digest % len(palette)]


def render_route_pills(route: list, active_skill: str, target_skill: str):
    if not route:
        return
    parts = []
    for s in route:
        if s not in graph.nodes:
            continue
        label = graph.nodes[s]["label"]
        mastery = graph.nodes[s].get("mastery", 0)
        if s == active_skill:
            css = "route-pill active"
        elif s == target_skill:
            css = "route-pill target"
        elif mastery >= TARGET_MASTERY:
            css = "route-pill done"
        else:
            css = "route-pill"
        parts.append(f'<span class="{css}">{label}</span>')
    st.markdown(" → ".join(parts), unsafe_allow_html=True)


# ── SCREEN: LEARNING ──────────────────────────────────────────────────────────

def render_learn_screen():
    target_skill = st.session_state.target_skill
    active_skill = st.session_state.active_skill
    route = st.session_state.learning_route

    has_target = bool(target_skill and target_skill in graph.nodes)

    if has_target:
        if not active_skill or active_skill not in graph.nodes:
            st.session_state.active_skill = target_skill
            active_skill = target_skill

        target_name = graph.nodes[target_skill]["label"]
        active_name = graph.nodes[active_skill]["label"]
        active_mastery = graph.nodes[active_skill].get("mastery", 0.2)
    else:
        target_skill = None
        active_skill = None
        target_name = ""
        active_name = ""
        active_mastery = 0.0

    route_node_set = set(route)

    # ── HEADER ────────────────────────────────────────────────────────────────

    if has_target:
        hcols = st.columns([2.2, 2.2, 1.6, 1.4])
        with hcols[0]:
            st.markdown(
                f'<div class="stat-label">Goal</div>'
                f'<div class="stat-value">🎯 {target_name}</div>',
                unsafe_allow_html=True,
            )
        with hcols[1]:
            st.markdown(
                f'<div class="stat-label">Currently practicing</div>'
                f'<div class="stat-value">📖 {active_name}</div>',
                unsafe_allow_html=True,
            )
        with hcols[2]:
            total_mins = route_time_estimate([s for s in route if s in graph.nodes])
            total_tasks = max(1, round(total_mins / MINS_PER_ATTEMPT))
            st.markdown(
                f'<div class="stat-label">Route estimate</div>'
                f'<div class="stat-value">⏱ {fmt_time(total_mins)} · ~{total_tasks} tasks</div>',
                unsafe_allow_html=True,
            )
        with hcols[3]:
            step = (route.index(active_skill) + 1) if active_skill in route else "—"
            st.markdown(
                f'<div class="stat-label">Route step</div>'
                f'<div class="stat-value">{step} / {len(route)}</div>',
                unsafe_allow_html=True,
            )
        st.divider()
    else:
        st.markdown(
            '<h2 style="margin:0 0 2px;color:#EAEFF7;font-weight:800">SkillGraph Tutor</h2>'
            '<p style="margin:0 0 12px;color:#6B7280;font-size:0.88rem">'
            'Explore, practice, and progress through connected math skills — '
            'click any node on the map to set your learning goal.</p>',
            unsafe_allow_html=True,
        )
        st.divider()

    graph_fullscreen = st.session_state.get("graph_fullscreen", False)
    if graph_fullscreen:
        graph_col = st.container()
        task_col = None
    else:
        graph_col, task_col = st.columns([1.85, 1])

    # ── GRAPH ─────────────────────────────────────────────────────────────────

    with graph_col:
        header_cols = st.columns([1, 0.18])
        with header_cols[0]:
            st.markdown("### Skill Map")
        with header_cols[1]:
            toggle_label = "⤢" if not graph_fullscreen else "⤡"
            if st.button(toggle_label, use_container_width=True):
                st.session_state.graph_fullscreen = not graph_fullscreen
                st.rerun()

        view_graph = build_view_graph(target_skill)

        selected_node = st.session_state.graph_selected or active_skill

        # ── Node sizes: percentile rank of PageRank → clear visual difference ─
        all_pr_sorted = np.array(
            sorted(pagerank_scores.get(n, 0) for n in view_graph.nodes)
        )

        def node_display_size(node_id: str) -> float:
            pr = pagerank_scores.get(node_id, 0)
            rank = float(np.searchsorted(all_pr_sorted, pr)) / max(len(all_pr_sorted) - 1, 1)
            return 50 + 190 * rank  # range 50–240 px

        node_sizes = {n: node_display_size(n) for n in view_graph.nodes}

        positions = get_spring_positions(view_graph)

        neighbors = set()
        if selected_node and selected_node in view_graph.nodes:
            neighbors.update(list(view_graph.predecessors(selected_node)))
            neighbors.update(list(view_graph.successors(selected_node)))

        nodes_payload = []
        for node_id in view_graph.nodes:
            x, y = positions.get(node_id, (0, 0))
            classes = []
            if node_id == selected_node:
                classes.append("key")
            if node_id in neighbors:
                classes.append("neighbor")
            if node_id in route_node_set:
                classes.append("route")

            node_area = graph.nodes[node_id].get("area") or "Other"
            node_data = graph.nodes[node_id]
            size = node_sizes[node_id]

            nodes_payload.append({
                "data": {
                    "id": node_id,
                    "label": node_data.get("label", str(node_id)),
                    "area": node_area,
                    "color": area_color(node_area),
                    "size": size,
                    "mastery": round(float(node_data.get("mastery", 0.2)), 3),
                    "levelBand": node_data.get("level_band", ""),
                },
                "position": {"x": float(x), "y": float(y)},
                "classes": " ".join(classes),
            })

        # Prereq edges — visibility controlled by zoom / selection in frontend
        edges_payload = [
            {
                "data": {
                    "id": f"e_{src}_{tgt}",
                    "source": src,
                    "target": tgt,
                }
            }
            for src, tgt, d in view_graph.edges(data=True)
            if d.get("edge_type") == "prereq"
        ]

        graph_height = 860 if graph_fullscreen else 740
        clicked_id = render_cytoscape_graph(
            nodes=nodes_payload,
            edges=edges_payload,
            height=graph_height,
            focus_node_id=selected_node,
            focus_zoom=1.15,
            key="cytoscape_graph",
        )

        # Guard: Cytoscape retains clicked_id permanently across all reruns.
        # We compare against _graph_click_absorbed (the last click we already handled)
        # rather than graph_selected, so answer-driven navigation never causes a re-fire.
        if (clicked_id and clicked_id in graph.nodes
                and clicked_id != st.session_state.get("_graph_click_absorbed")):
            resolved = resolve_atomic(clicked_id)
            # Clicking a skill always sets it as the new GOAL and rebuilds the route.
            new_route = build_learning_route(graph, resolved, pagerank_scores, MASTERY_THRESHOLD)
            st.session_state.target_skill = resolved
            st.session_state.active_skill = resolved  # start at the goal; drill back only if stuck
            st.session_state.graph_selected = clicked_id
            st.session_state._graph_click_absorbed = clicked_id
            st.session_state.learning_route = new_route
            st.session_state.last_feedback = None
            st.session_state.show_hint = False
            st.session_state.show_answer = False
            st.session_state.consecutive_wrong = {}
            st.rerun()

        # Fallback navigation dropdown
        atomic_in_view = sorted(
            [(nid, graph.nodes[nid]["label"]) for nid in view_graph.nodes
             if graph.nodes[nid].get("node_type") == "atomic_skill"],
            key=lambda x: x[1],
        )
        if atomic_in_view:
            labels = [lbl for _, lbl in atomic_in_view]
            id_map = {lbl: nid for nid, lbl in atomic_in_view}
            curr_label = graph.nodes[active_skill]["label"] if active_skill and active_skill in graph.nodes else labels[0]
            idx = labels.index(curr_label) if curr_label in labels else 0
            picked = st.selectbox("Navigate to skill", labels, index=idx)
            picked_id = id_map[picked]
            if picked_id != active_skill:
                resolved = resolve_atomic(picked_id)
                # Selecting via dropdown always sets the skill as the new goal.
                new_route = build_learning_route(graph, resolved, pagerank_scores, MASTERY_THRESHOLD)
                st.session_state.target_skill = resolved
                st.session_state.active_skill = resolved  # start at the goal; drill back only if stuck
                st.session_state.graph_selected = picked_id
                # Absorb any pending Cytoscape click so it doesn't override this navigation.
                st.session_state._graph_click_absorbed = clicked_id
                st.session_state.learning_route = new_route
                st.session_state.last_feedback = None
                st.session_state.show_hint = False
                st.session_state.show_answer = False
                st.session_state.consecutive_wrong = {}
                st.rerun()

        # ── Area color legend ─────────────────────────────────────────────
        unique_areas = sorted({
            graph.nodes[n].get("area") or "Other"
            for n in view_graph.nodes
        })
        swatches = "".join(
            f'<span style="display:inline-flex;align-items:center;gap:4px;'
            f'margin:2px 10px 2px 0;font-size:0.70rem;color:#6B7280;white-space:nowrap">'
            f'<span style="display:inline-block;width:8px;height:8px;border-radius:50%;flex-shrink:0;'
            f'background:{area_color(a)};box-shadow:0 0 5px {area_color(a)}66"></span>{a}</span>'
            for a in unique_areas
        )
        st.markdown(
            f'<div style="background:#070A12;border:1px solid rgba(234,239,247,0.07);'
            f'border-radius:10px;padding:8px 12px;margin:6px 0 10px;line-height:2.0">'
            f'{swatches}</div>',
            unsafe_allow_html=True,
        )

        if has_target:
            # Route pills
            st.markdown("**Route:**")
            render_route_pills(route, active_skill, target_skill)

            # Knowledge gaps (PageRank-weighted) ── live: updates every rerun
            with st.expander("🔍 Top knowledge gaps blocking goal"):
                recs = calculate_review_recommendations(graph, target_skill, pagerank_scores)
                gaps = [r for r in recs if r["mastery"] < MASTERY_THRESHOLD][:8]
                if not recs:
                    st.info("Foundational skill — no prerequisites to review.")
                elif not gaps:
                    st.success(f"All {len(recs)} prerequisite(s) are above the mastery threshold — you're prepared!")
                else:
                    # Show whether the current practice skill is one of these gaps,
                    # so the student understands the connection to the task panel.
                    gap_ids = [g["skill_id"] for g in gaps]
                    if active_skill in gap_ids:
                        st.markdown(
                            f'<div style="background:rgba(255,107,107,0.08);border:1px solid rgba(255,107,107,0.25);'
                            f'border-radius:8px;padding:7px 10px;margin-bottom:10px;font-size:0.80rem;color:#FF6B6B">'
                            f'▶ Currently practicing: <b>{active_name}</b> — '
                            f'this is why it\'s assigned in the task panel.</div>',
                            unsafe_allow_html=True,
                        )
                    else:
                        st.caption(
                            "When you answer incorrectly, the system automatically navigates "
                            "you to the highest-priority gap. Mastery updates live as you practice."
                        )
                    for gap in gaps:
                        m = gap["mastery"]
                        pct_g = int(m * 100)
                        mc = "#8DE4AF" if m >= 0.7 else "#F6D06F" if m >= 0.4 else "#FF6B6B"
                        dist = gap["distance_to_target"]
                        is_active = gap["skill_id"] == active_skill
                        name_color = "#00E5FF" if is_active else "#EAEFF7"
                        active_marker = " ◀ practicing now" if is_active else ""
                        st.markdown(
                            f'<div style="margin:8px 0;padding:6px 0;'
                            f'{"border-left:2px solid #00E5FF;padding-left:8px;" if is_active else ""}">'
                            f'<div style="display:flex;justify-content:space-between;margin-bottom:3px">'
                            f'<span style="font-size:0.82rem;font-weight:600;color:{name_color}">'
                            f'{gap["skill_name"]}{active_marker}</span>'
                            f'<span style="font-size:0.75rem;color:#6B7280">{dist} step{"s" if dist!=1 else ""} away</span>'
                            f'</div>'
                            f'<div style="background:#0B1020;border-radius:999px;height:4px;overflow:hidden">'
                            f'<div style="width:{pct_g}%;background:{mc};height:100%;border-radius:999px"></div>'
                            f'</div>'
                            f'<div style="font-size:0.72rem;color:{mc};margin-top:2px">{pct_g}%</div>'
                            f'</div>',
                            unsafe_allow_html=True,
                        )

            # PageRank sidebar — shows relative importance as percentile
            with st.expander("📊 PageRank — skill importance on path to goal"):
                prereq_sub = nx.DiGraph()
                for u, v, d in graph.edges(data=True):
                    if d.get("edge_type") == "prereq":
                        prereq_sub.add_edge(u, v)
                ancestors = [
                    n for n in (nx.ancestors(prereq_sub, target_skill) if target_skill in prereq_sub else set())
                    if graph.nodes.get(n, {}).get("node_type") == "atomic_skill"
                ]
                # Normalise PageRank to percentile within the full graph for interpretability
                all_pr = sorted(pagerank_scores.values())
                def pr_percentile(node_id):
                    v = pagerank_scores.get(node_id, 0)
                    idx = np.searchsorted(all_pr, v, side="left")
                    return int(100 * idx / max(len(all_pr) - 1, 1))

                active_pr_pct = pr_percentile(active_skill)
                if not ancestors:
                    st.info("Foundational skill — no prerequisites in the graph.")
                    pct = pr_percentile(target_skill)
                    st.caption(f"**{active_name}** sits at the **{pct}th percentile** of curriculum importance.")
                else:
                    pr_rows = sorted(
                        [
                            {
                                "Skill": graph.nodes[n]["label"],
                                "_pr": pagerank_scores.get(n, 0),
                                "Importance": f"{pr_percentile(n)}th %ile",
                                "Mastery": f"{graph.nodes[n].get('mastery', 0):.0%}",
                                "_id": n,
                            }
                            for n in ancestors
                        ],
                        key=lambda r: -r["_pr"],
                    )[:10]
                    # Highlight the row for the currently active skill.
                    if active_skill in [r["_id"] for r in pr_rows]:
                        st.markdown(
                            f'<div style="background:rgba(125,211,252,0.08);border:1px solid rgba(125,211,252,0.20);'
                            f'border-radius:8px;padding:7px 10px;margin-bottom:8px;font-size:0.80rem;color:#7DD3FC">'
                            f'▶ Currently practicing: <b>{active_name}</b> — '
                            f'{active_pr_pct}th %ile importance</div>',
                            unsafe_allow_html=True,
                        )
                    pr_df = pd.DataFrame(pr_rows)[["Skill", "Importance", "Mastery"]]
                    st.dataframe(pr_df, use_container_width=True, hide_index=True)
                    st.caption(
                        "**Importance** = PageRank percentile across the full curriculum. "
                        "A skill at the 90th %ile unlocks more downstream content than 90 % of all skills. "
                        "The task panel automatically prioritises high-importance gaps."
                    )

    # ── TASK PANEL ────────────────────────────────────────────────────────────

    if task_col:
        with task_col:
            if not has_target or not active_skill:
                st.markdown(
                    '<div style="background:#070A12;border:1px solid rgba(234,239,247,0.09);'
                    'border-radius:16px;padding:28px 24px;margin-top:24px;text-align:center">'
                    '<div style="font-size:2.2rem;margin-bottom:12px">🌌</div>'
                    '<div style="font-size:1.1rem;font-weight:800;color:#EAEFF7;margin-bottom:8px">Select a skill</div>'
                    '<div style="font-size:0.88rem;color:#6B7280;line-height:1.6">'
                    'Click any node on the skill map to set it as your learning goal. '
                    'The system will build a personalised practice route for you.'
                    '</div></div>',
                    unsafe_allow_html=True,
                )
                return

            # Skill header card
            node_area_name = graph.nodes[active_skill].get("area") or "Other"
            m_color = "#8DE4AF" if active_mastery >= 0.7 else "#F6D06F" if active_mastery >= 0.4 else "#FF6B6B"
            st.markdown(
                f'<div class="task-header">'
                f'<div class="task-skill-name">{active_name}</div>'
                f'<span class="task-area-pill">{node_area_name}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )
            # Mastery progress bar
            pct = min(100, int(active_mastery * 100))
            st.markdown(
                f'<div style="margin:0 0 10px">'
                f'<div style="display:flex;justify-content:space-between;margin-bottom:5px">'
                f'<span style="font-size:0.78rem;color:#9AA4B2;font-weight:600">Mastery</span>'
                f'<span style="font-size:0.78rem;font-weight:700;color:{m_color}">{pct}%</span>'
                f'</div>'
                f'<div style="background:#0B1020;border-radius:999px;height:5px;overflow:hidden">'
                f'<div style="width:{pct}%;background:{m_color};height:100%;border-radius:999px"></div>'
                f'</div></div>',
                unsafe_allow_html=True,
            )

            # ── "Why this skill?" context ─────────────────────────────────
            # Pulls from the same PageRank + gap data used in the left panel
            # so the task panel and the analytics expanders tell a coherent story.
            if has_target and target_skill:
                _why_parts = []

                # Is this skill a knowledge gap blocking the goal?
                _gap_recs = calculate_review_recommendations(graph, target_skill, pagerank_scores)
                _gap_ids = [r["skill_id"] for r in _gap_recs if r["mastery"] < MASTERY_THRESHOLD]
                if active_skill == target_skill:
                    _why_parts.append(("🎯", "#00E5FF", "This is your current learning goal"))
                elif active_skill in _gap_ids:
                    _gap_rank = _gap_ids.index(active_skill) + 1
                    _why_parts.append(("🔍", "#FF6B6B",
                        f"Gap #{_gap_rank} blocking your goal — low mastery prerequisite"))

                # PageRank percentile
                _all_pr = sorted(pagerank_scores.values())
                _pr_pct = int(100 * np.searchsorted(_all_pr, pagerank_scores.get(active_skill, 0))
                              / max(len(_all_pr) - 1, 1))
                if _pr_pct >= 75:
                    _why_parts.append(("📊", "#7DD3FC",
                        f"High-importance skill — {_pr_pct}th %ile in the curriculum"))
                elif _pr_pct >= 50:
                    _why_parts.append(("📊", "#9AA4B2",
                        f"Moderate importance — {_pr_pct}th %ile"))

                if _why_parts:
                    _badges = "".join(
                        f'<div style="display:flex;align-items:flex-start;gap:7px;'
                        f'margin-bottom:5px">'
                        f'<span style="font-size:0.9rem;line-height:1.4">{icon}</span>'
                        f'<span style="font-size:0.78rem;color:{color};line-height:1.4">{text}</span>'
                        f'</div>'
                        for icon, color, text in _why_parts
                    )
                    st.markdown(
                        f'<div style="background:#070A12;border:1px solid rgba(234,239,247,0.08);'
                        f'border-radius:10px;padding:9px 12px;margin-bottom:12px">'
                        f'<div style="font-size:0.68rem;color:#6B7280;text-transform:uppercase;'
                        f'letter-spacing:0.07em;margin-bottom:7px">Why this skill?</div>'
                        f'{_badges}</div>',
                        unsafe_allow_html=True,
                    )

            # Feedback from last attempt
            fb = st.session_state.last_feedback
            if fb and fb.get("stuck"):
                st.warning(
                    "You've struggled with this skill 3 times in a row — "
                    "the answer is shown below. Review it, then try the next question.",
                    icon="🔓",
                )
            if fb:
                prev_skill = fb.get("skill_name", "")
                prev_label = f" on **{prev_skill}**" if prev_skill and prev_skill != active_name else ""
                moved = fb.get("moved", False)
                next_skill_name = fb.get("next_skill_name", "")
                nav_note = (
                    f"<br><small style='font-weight:normal'>→ Moving to: <b>{next_skill_name}</b></small>"
                    if moved and next_skill_name and next_skill_name != prev_skill else ""
                )
                next_reason = fb.get("next_reason", "")
                delta = fb["after"] - fb["before"]
                delta_str = f"+{delta:.0%}" if delta >= 0 else f"{delta:.0%}"
                if fb["result"] == "Correct":
                    st.markdown(
                        f'<div class="fb-correct">✅ Correct{prev_label}! '
                        f'Mastery {fb["before"]:.0%} → {fb["after"]:.0%} ({delta_str})'
                        f'{nav_note}'
                        f'<br><small style="font-weight:normal">{next_reason}</small></div>',
                        unsafe_allow_html=True,
                    )
                elif fb["result"] == "I don't know":
                    exp = fb.get("expected_answer", "")
                    exp_str = f"<br><small style='font-weight:normal'>Answer was: <b>{exp}</b></small>" if exp else ""
                    st.markdown(
                        f'<div class="fb-idk">💡 No worries{prev_label} — let\'s build from the foundation'
                        f'{exp_str}'
                        f'{nav_note}'
                        f'<br><small style="font-weight:normal">{next_reason}</small></div>',
                        unsafe_allow_html=True,
                    )
                elif fb["result"] == "Partial":
                    st.markdown(
                        f'<div class="fb-partial">🔶 Partial answer{prev_label}. '
                        f'Mastery {fb["before"]:.0%} → {fb["after"]:.0%} ({delta_str})'
                        f'{nav_note}'
                        f'<br><small style="font-weight:normal">{next_reason}</small></div>',
                        unsafe_allow_html=True,
                    )
                else:
                    exp = fb.get("expected_answer", "")
                    exp_str = f"<br><small style='font-weight:normal'>Expected: <b>{exp}</b></small>" if exp else ""
                    st.markdown(
                        f'<div class="fb-wrong">❌ Not quite{prev_label}. '
                        f'Mastery {fb["before"]:.0%} → {fb["after"]:.0%} ({delta_str})'
                        f'{exp_str}'
                        f'{nav_note}'
                        f'<br><small style="font-weight:normal">{next_reason}</small></div>',
                        unsafe_allow_html=True,
                    )

                recs = fb.get("recommendations", [])
                if recs:
                    rec_html = "".join(
                        f'<span style="display:inline-block;margin:3px 4px;padding:3px 10px;'
                        f'border-radius:999px;background:#1e293b;border:1px solid #334155;'
                        f'font-size:0.78rem;color:#cbd5e1">'
                        f'<b>{r["skill_name"]}</b>'
                        f'<span style="color:#64748b"> — {r["reason"]}</span></span>'
                        for r in recs
                    )
                    st.markdown(
                        f'<div style="margin-top:8px"><span style="font-size:0.78rem;'
                        f'color:#64748b;font-weight:600">💡 You might also like: </span>'
                        f'{rec_html}</div>',
                        unsafe_allow_html=True,
                    )

            # ── Time / attempts to mastery ────────────────────────────────────
            history = mastery_history_for(active_skill)
            lr_attempts, r2 = linear_regression_prediction(history, TARGET_MASTERY)
            if lr_attempts is not None and r2 is not None and r2 > 0.4:
                lr_mins = lr_attempts * MINS_PER_ATTEMPT
                st.caption(
                    f"📈 **Linear regression** (R²={r2:.2f}): "
                    f"~**{lr_attempts:.0f} more attempts** · {fmt_time(lr_mins)}"
                )
            else:
                attempts, reachable = skill_time_estimate(active_skill)
                # skill_time_estimate returns (minutes, reachable) — convert back to attempts
                raw_attempts = int(attempts / MINS_PER_ATTEMPT) if reachable else None
                if reachable and raw_attempts is not None:
                    st.caption(
                        f"⏱ **Model estimate**: ~{raw_attempts} attempts · {fmt_time(attempts)}"
                    )
                else:
                    st.caption(f"⏱ **Model estimate**: >{fmt_time(40 * MINS_PER_ATTEMPT)} (requires many sessions)")

            st.divider()

            # Task generation
            current_task = generated_task_for_skill(
                tasks_df=tasks_data,
                skill_id=active_skill,
                mastery=active_mastery,
                seed=st.session_state.task_counter,
                skill_title=graph.nodes[active_skill].get("label"),
            )

            if current_task is None:
                current_task = {
                    "difficulty": "practice",
                    "task_title": "Explain in your own words",
                    "task_latex": "",
                    "task_text": "Write one sentence: what is this skill and why does it matter?",
                    "expected_answer": "",
                    "accepted_answers": "__any__",
                    "hint": "Focus on the core idea or procedure.",
                }

            # Task header: title + per-task time estimate
            task_h, task_t = st.columns([3, 1])
            with task_h:
                st.markdown(f"#### {current_task['task_title']}")
            with task_t:
                st.markdown(
                    f"<div style='text-align:right;padding-top:8px;font-size:0.8rem;"
                    f"color:#9ca3af'>⏱ ~{MINS_PER_ATTEMPT} min</div>",
                    unsafe_allow_html=True,
                )
            st.caption(f"Difficulty: {current_task['difficulty']}")

            if str(current_task.get("task_latex", "")).strip():
                st.latex(current_task["task_latex"])
            if str(current_task.get("task_text", "")).strip():
                st.markdown(current_task["task_text"])

            user_answer = st.text_input(
                "Answer",
                key=f"ans_{active_skill}_{st.session_state.task_counter}",
                placeholder="Type your answer...",
            )

            b1, b2 = st.columns(2)
            b3, b4 = st.columns(2)

            with b1:
                check_clicked = st.button("✓ Check", use_container_width=True, type="primary")
            with b2:
                idk_clicked = st.button("? Don't know", use_container_width=True)
            with b3:
                if st.button("💡 Hint", use_container_width=True):
                    st.session_state.show_hint = not st.session_state.show_hint
                    st.session_state.show_answer = False
            with b4:
                if st.button("👁 Show answer", use_container_width=True):
                    st.session_state.show_answer = not st.session_state.show_answer
                    st.session_state.show_hint = False

            if st.session_state.show_hint:
                st.info(f"💡 {current_task.get('hint', 'Think about the main definition.')}")
            if st.session_state.show_answer:
                exp = current_task.get("expected_answer", "")
                st.success(f"Answer: **{exp}**" if exp else "Open answer — any explanation works.")

            # ── Demo mode buttons ─────────────────────────────────────────────
            st.markdown(
                '<div class="demo-bar"><div class="demo-label">🎬 Demo — simulate result</div>',
                unsafe_allow_html=True,
            )
            d1, d2, d3 = st.columns(3)
            with d1:
                demo_correct = st.button("✅ Correct",  use_container_width=True, key="demo_correct")
            with d2:
                demo_partial = st.button("🔶 Partial",  use_container_width=True, key="demo_partial")
            with d3:
                demo_wrong   = st.button("❌ Wrong",    use_container_width=True, key="demo_wrong")
            st.markdown("</div>", unsafe_allow_html=True)

            # ── Process answer (real or demo) ─────────────────────────────────
            any_answer = check_clicked or idk_clicked or demo_correct or demo_partial or demo_wrong
            if any_answer:
                if demo_correct:
                    result_label, result_score = "Correct", 1.0
                elif demo_partial:
                    result_label, result_score = "Partial", 0.5
                elif demo_wrong:
                    result_label, result_score = "Wrong", 0.15
                elif check_clicked:
                    is_correct = check_answer(user_answer, current_task["accepted_answers"])
                    result_label = "Correct" if is_correct else "Wrong"
                    result_score = 1.0 if is_correct else 0.15
                else:
                    result_label, result_score = "I don't know", 0.0

                before = st.session_state.mastery.get(active_skill, 0.2)

                updated_mastery = apply_practice_result(
                    mastery_dict=st.session_state.mastery,
                    graph=graph,
                    target_skill=active_skill,
                    result_score=result_score,
                    learning_gain=LEARNING_GAIN,
                    prerequisite_gain=PREREQ_GAIN,
                )
                st.session_state.mastery = updated_mastery
                after = updated_mastery.get(active_skill, before)

                # Rebuild graph with updated mastery for navigation
                new_graph = build_curriculum_graph(nodes_df, graph_df, mastery_dict=updated_mastery)
                new_pr = calculate_pagerank(new_graph, edge_type="prereq")

                # Include active_skill + recently practiced to avoid A→B→A cycles.
                # active_skill is added first because the log entry isn't appended yet.
                recent_ids = list(dict.fromkeys(
                    [active_skill] + [e["skill_id"] for e in reversed(st.session_state.practice_log[-10:])]
                ))[:6]

                # Track consecutive Wrong/IDK on the same skill to detect stuck state.
                cw = st.session_state.consecutive_wrong
                if result_label in ("Wrong", "I don't know"):
                    cw[active_skill] = cw.get(active_skill, 0) + 1
                else:
                    cw[active_skill] = 0
                st.session_state.consecutive_wrong = cw
                is_stuck = cw.get(active_skill, 0) >= 3

                next_skill, next_route, next_reason = choose_next_after_attempt(
                    graph=new_graph,
                    active_skill=active_skill,
                    target_skill=target_skill,
                    result_label=result_label,
                    pagerank_scores=new_pr,
                    local_mastery_threshold=MASTERY_THRESHOLD,
                    current_route=st.session_state.learning_route,
                    exclude_ids=recent_ids,
                )

                st.session_state.practice_log.append({
                    "skill_id": active_skill,
                    "skill_name": active_name,
                    "result": result_label,
                    "before": before,
                    "after": after,
                    "task": current_task["task_title"],
                })

                next_skill = resolve_atomic(next_skill)
                next_skill_name = new_graph.nodes[next_skill].get("label", "") if next_skill in new_graph.nodes else ""

                skill_recs = recommend_related_skills(
                    new_graph, active_skill, updated_mastery, new_pr, top_n=3
                )

                st.session_state.task_counter += 1
                st.session_state.active_skill = next_skill
                st.session_state.learning_route = next_route
                st.session_state.graph_selected = next_skill
                # Absorb the current Cytoscape click so the guard doesn't re-fire on future reruns.
                st.session_state._graph_click_absorbed = clicked_id
                st.session_state.last_feedback = {
                    "result": result_label,
                    "skill_name": active_name,
                    "next_skill_name": next_skill_name,
                    "moved": next_skill != active_skill,
                    "before": before,
                    "after": after,
                    "expected_answer": current_task.get("expected_answer", ""),
                    "next_reason": next_reason,
                    "recommendations": skill_recs,
                    "stuck": is_stuck,
                }
                st.session_state.show_hint = False
                # After 3 consecutive wrong on same skill, reveal the answer automatically.
                st.session_state.show_answer = is_stuck
                st.rerun()


# ── MAIN ──────────────────────────────────────────────────────────────────────

render_learn_screen()
