import plotly.graph_objects as go
import numpy as np


ACCENT = "#16A34A"
ACCENT_SOFT = "#A7F3D0"
NODE_BASE = "#D1D5DB"
NODE_TEXT = "#111827"
EDGE_BASE = "rgba(17, 24, 39, 0.18)"
EDGE_ROUTE = "rgba(22, 163, 74, 0.7)"
GRID_BG = "#FFFFFF"


def node_fill_color(skill_id, key_skill, neighbor_nodes, faded=False):
    if skill_id == key_skill:
        return ACCENT
    if skill_id in neighbor_nodes:
        return ACCENT_SOFT
    return "#E5E7EB" if faded else NODE_BASE


def border_color(skill_id, key_skill, route_nodes):
    if skill_id == key_skill:
        return ACCENT
    if skill_id in route_nodes:
        return "#6B7280"
    return "#9CA3AF"


def node_size(skill_id, pagerank_scores, route_nodes):
    importance = pagerank_scores.get(skill_id, 0)

    if skill_id in route_nodes:
        size = 36 + importance * 200
    else:
        size = 22 + importance * 100

    return min(max(size, 24), 58)


def node_position(data):
    level = int(data.get("level", 0))
    return level * 220, 0


def build_plotly_graph(
    graph,
    pagerank_scores,
    target_skill,
    active_skill,
    recommended_skill,
    graph_selected_skill,
    positions=None,
    route_nodes=None,
    route_edges=None,
):
    if route_nodes is None:
        route_nodes = set()

    if route_edges is None:
        route_edges = set()

    if graph.number_of_nodes() == 0:
        fig = go.Figure()
        fig.update_layout(
            showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False, visible=False),
            yaxis=dict(showgrid=False, zeroline=False, visible=False),
            margin=dict(l=10, r=10, t=10, b=10),
            height=720,
            annotations=[
                dict(
                    text="No nodes to display",
                    x=0.5,
                    y=0.5,
                    xref="paper",
                    yref="paper",
                    showarrow=False,
                    font=dict(size=16, color="#6B7280"),
                )
            ],
        )
        return fig

    # --- Node processing ---
    node_x, node_y = [], []
    node_text, node_color, node_opacity = [], [], []
    node_size_values, node_border_color, node_border_width = [], [], []
    node_labels = []
    node_custom = []
    positions = positions or {}
    used_positions = {}

    key_skill = graph_selected_skill or active_skill
    neighbors = set()
    if key_skill in graph.nodes:
        neighbors.update(list(graph.predecessors(key_skill)))
        neighbors.update(list(graph.successors(key_skill)))

    important_nodes = set(route_nodes)
    important_nodes.update({target_skill, active_skill, key_skill})

    def clean_text(value, fallback):
        if value is None:
            return fallback
        if isinstance(value, float) and np.isnan(value):
            return fallback
        text = str(value).strip()
        if text == "" or text.lower() == "nan":
            return fallback
        return text

    for skill_id in sorted(list(graph.nodes()), key=lambda value: str(value)):
        data = graph.nodes[skill_id]
        mastery = data.get("mastery", 0.2)
        if skill_id in positions:
            x, y = positions[skill_id]
        else:
            x, y = node_position(data)

        key = (x, y)
        offset = used_positions.get(key, 0)
        used_positions[key] = offset + 1
        y -= offset * 78
        positions[skill_id] = (x, y)

        faded = skill_id not in important_nodes

        node_x.append(x)
        node_y.append(y)
        node_color.append(node_fill_color(skill_id, key_skill, neighbors, faded=faded))
        node_opacity.append(0.35 if faded else 0.98)
        node_size_values.append(node_size_for_plotly(skill_id, pagerank_scores, route_nodes))
        node_custom.append(skill_id)

        b_color, b_width = border_color_and_width_for_plotly(
            skill_id, key_skill, route_nodes
        )
        node_border_color.append(b_color)
        node_border_width.append(b_width)

        if hasattr(graph, "in_degree"):
            prereq_count = graph.in_degree(skill_id)
            next_count = graph.out_degree(skill_id)
        else:
            prereq_count = graph.degree(skill_id)
            next_count = graph.degree(skill_id)
        label = clean_text(data.get("label"), str(skill_id))
        group_label = clean_text(data.get("group"), "Unknown")
        node_text.append(
            f"<b>{label}</b><br>"
            f"Level: {mastery:.0%}<br>"
            f"Group: {group_label}<br>"
            f"Prereqs: {prereq_count} · Unlocks: {next_count}"
        )
        
        node_labels.append(label)

    # --- Edge processing ---
    fig = go.Figure()

    # Create a trace for each edge type to control color and width
    route_edge_x, route_edge_y = [], []
    other_edge_x, other_edge_y = [], []

    for source, target, data in graph.edges(data=True):
        if source not in positions or target not in positions:
            continue

        x0, y0 = positions[source]
        x1, y1 = positions[target]
        
        is_route_edge = (source, target) in route_edges

        if is_route_edge:
            route_edge_x.extend([x0, x1, None])
            route_edge_y.extend([y0, y1, None])
        else:
            other_edge_x.extend([x0, x1, None])
            other_edge_y.extend([y0, y1, None])

    fig.add_trace(go.Scatter(
        x=other_edge_x,
        y=other_edge_y,
        mode="lines",
        line=dict(width=0.7, color=EDGE_BASE),
        hoverinfo="none",
    ))

    fig.add_trace(go.Scatter(
        x=route_edge_x,
        y=route_edge_y,
        mode="lines",
        line=dict(width=2.4, color=EDGE_ROUTE),
        hoverinfo="none",
    ))

    # --- Node Trace ---
    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        hoverinfo="text",
        text=node_labels,
        textposition="top center",
        textfont=dict(size=12, color=NODE_TEXT),
        hovertext=node_text,
        customdata=node_custom,
        marker=dict(
            color=node_color,
            opacity=node_opacity,
            size=node_size_values,
            line=dict(width=node_border_width, color=node_border_color),
        ),
    )
    fig.add_trace(node_trace)

    # --- Arrows ---
    arrow_annotations = []
    for source, target in graph.edges():
        if source not in positions or target not in positions:
            continue
        
        x0, y0 = positions[source]
        x1, y1 = positions[target]
        
        is_route_edge = (source, target) in route_edges
        arrow_color = EDGE_ROUTE if is_route_edge else EDGE_BASE

        # Shorten the arrow to avoid overlapping the node marker
        vec = np.array([x1 - x0, y1 - y0])
        vec_len = np.linalg.norm(vec)
        if vec_len == 0: continue
        
        node_radius = node_size_for_plotly(target, pagerank_scores, route_nodes) / 2
        
        # Heuristic for scaling factor
        scale_factor = (vec_len - node_radius - 5) / vec_len
        
        if scale_factor < 0: scale_factor = 0.1

        ax = x0 + vec[0] * scale_factor
        ay = y0 + vec[1] * scale_factor
        
        arrow_annotations.append(
            go.layout.Annotation(
                ax=ax, ay=ay, x=x0, y=y0,
                xref='x', yref='y', axref='x', ayref='y',
                showarrow=True,
                arrowhead=2,
                arrowsize=1.2,
                arrowwidth=1 if is_route_edge else 0.6,
                arrowcolor=arrow_color
            )
        )

    fig.update_layout(
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        margin=dict(l=10, r=10, t=10, b=10),
        height=800, # Increased height
        hovermode='closest',
        annotations=arrow_annotations,
        plot_bgcolor=GRID_BG,
        paper_bgcolor=GRID_BG,
        font=dict(color=NODE_TEXT),
        hoverlabel=dict(
            bgcolor=GRID_BG,
            bordercolor="#D1D5DB",
            font=dict(color=NODE_TEXT),
        ),
    )

    return fig


def node_size_for_plotly(skill_id, pagerank_scores, route_nodes):
    importance = pagerank_scores.get(skill_id, 0)
    if skill_id in route_nodes:
        size = 32 + importance * 180
    else:
        size = 20 + importance * 100
    return min(max(size, 20), 52)


def border_color_and_width_for_plotly(skill_id, key_skill, route_nodes):
    if skill_id == key_skill:
        return ACCENT, 3.5
    if skill_id in route_nodes:
        return "#6B7280", 2
    return "#9CA3AF", 1.2
