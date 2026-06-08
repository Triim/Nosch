import math
import networkx as nx


# ---------------------------------------------------------------------------
# Module-level cache for augmented prerequisite edges.
# Populated once by _build_extra_prereq_edges(); keyed by (src_id, tgt_id).
# ---------------------------------------------------------------------------
_EXTRA_PREREQ_EDGES: dict[tuple, dict] = {}
_EXTRA_PREREQ_EDGES_VERSION = 2  # bump to force rebuild after algorithm changes

LEVEL_BAND_ORDER = [
    "foundation",
    "school_algebra",
    "transition_to_university",
    "undergraduate_core",
    "advanced_undergraduate",
]


def _build_extra_prereq_edges(nodes_df, graph_df) -> dict[tuple, dict]:
    """Build a set of augmented prerequisite edges to enrich the curriculum graph.

    Strategy
    --------
    - Only atomic skills are considered.
    - Skills are grouped by ``level_band`` according to LEVEL_BAND_ORDER.
    - For each atomic skill that has fewer than 3 existing ``prereq``-type
      atomic predecessors, we inject edges from "gateway" skills that live
      exactly one level band below the target skill.
    - Gateways are defined as the top-20 % most-connected atomic skills in the
      previous level band, measured by out-degree in the existing prereq graph.
    - At most 4 gateway edges are added per skill; edges only flow strictly
      from level[i-1] → level[i] to guarantee no cycles are introduced.

    Returns
    -------
    dict mapping ``(src_id, tgt_id)`` to ``{"weight": 0.4, "edge_type": "prereq"}``.
    """
    import pandas as pd

    # ── Build a temporary bare prereq graph for out-degree measurement ─────
    prereq_graph = nx.DiGraph()

    for _, row in nodes_df.iterrows():
        nid = row["node_id"]
        nt = str(row.get("node_type", "")).strip()
        lb = str(row.get("level_band", "")).strip()
        area = str(row.get("area", "")).strip()
        if nt == "atomic_skill":
            prereq_graph.add_node(nid, level_band=lb, node_type=nt, area=area)

    for _, row in graph_df.iterrows():
        node_id = row.get("node_id")
        prerequisites = row.get("prerequisite_ids")
        if not node_id or not isinstance(prerequisites, str) or not prerequisites.strip():
            continue
        for prereq_id in prerequisites.split("|"):
            prereq_id = prereq_id.strip()
            if prereq_id and prereq_id in prereq_graph and node_id in prereq_graph:
                prereq_graph.add_edge(prereq_id, node_id)

    # ── Group atomic skills by level band ─────────────────────────────────
    band_to_skills: dict[str, list] = {b: [] for b in LEVEL_BAND_ORDER}
    for nid, data in prereq_graph.nodes(data=True):
        lb = data.get("level_band", "")
        if lb in band_to_skills:
            band_to_skills[lb].append(nid)

    # ── Compute gateways for each level band (top-20% by out-degree) ──────
    band_gateways: dict[str, list] = {}
    for band, skills in band_to_skills.items():
        if not skills:
            band_gateways[band] = []
            continue
        scored = sorted(skills, key=lambda s: prereq_graph.out_degree(s), reverse=True)
        cutoff = max(1, math.ceil(len(scored) * 0.20))
        band_gateways[band] = scored[:cutoff]

    # ── Identify existing atomic prereq counts per skill ──────────────────
    existing_atomic_prereq_count: dict[str, int] = {}
    for nid in prereq_graph.nodes:
        existing_atomic_prereq_count[nid] = sum(
            1 for p in prereq_graph.predecessors(nid)
            if prereq_graph.nodes[p].get("node_type") == "atomic_skill"
        )

    # ── Build extra edges (same-area preferred, cross-area as fallback) ──────
    extra: dict[tuple, dict] = {}
    for band_idx, band in enumerate(LEVEL_BAND_ORDER):
        if band_idx == 0:
            continue
        prev_band = LEVEL_BAND_ORDER[band_idx - 1]
        gateways = band_gateways.get(prev_band, [])
        if not gateways:
            continue

        for tgt in band_to_skills.get(band, []):
            if existing_atomic_prereq_count.get(tgt, 0) >= 3:
                continue

            tgt_area = prereq_graph.nodes[tgt].get("area", "")

            # Pass 1: same-area gateways (strongest semantic signal)
            added = 0
            for gw in gateways:
                if added >= 3:
                    break
                if gw == tgt or prereq_graph.has_edge(gw, tgt):
                    continue
                if prereq_graph.nodes[gw].get("area", "") == tgt_area:
                    extra[(gw, tgt)] = {"weight": 0.6, "edge_type": "prereq"}
                    added += 1

            # Pass 2: fill remaining slots with cross-area gateways (weaker)
            for gw in gateways:
                if added >= 4:
                    break
                if gw == tgt or prereq_graph.has_edge(gw, tgt):
                    continue
                if (gw, tgt) in extra:
                    continue
                extra[(gw, tgt)] = {"weight": 0.3, "edge_type": "prereq"}
                added += 1

    return extra


GROUP_ORDER = {
    "Algebra": 9,
    "Functions": 6,
    "Derivatives": 3,
    "Root finding": 0,
    "Matrices": -3,
    
    "PageRank": -6,
    "Linear Regression": -8,
    "Interpolation": -9,
    "Optimization": -11,
    "Splines": -12,
}


def build_skill_graph(skills_df, dependencies_df, mastery_dict=None):
    graph = nx.DiGraph()

    for _, row in skills_df.iterrows():
        skill_id = row["skill_id"]

        if mastery_dict is None:
            mastery = float(row["initial_mastery"])
        else:
            mastery = float(mastery_dict[skill_id])

        graph.add_node(
            skill_id,
            label=row["skill_name"],
            group=row["group"],
            level=int(row["level"]),
            mastery=mastery,
        )

    for _, row in dependencies_df.iterrows():
        graph.add_edge(
            row["prerequisite"],
            row["target"],
            weight=float(row["weight"]),
        )

    return graph


def build_curriculum_graph(nodes_df, graph_df, mastery_dict=None):
    global _EXTRA_PREREQ_EDGES

    # Build the extra-edge cache once (it is expensive to recompute every render).
    # We use the size of the nodes_df as a cheap proxy to detect data changes.
    if len(_EXTRA_PREREQ_EDGES) == 0:
        _EXTRA_PREREQ_EDGES.update(_build_extra_prereq_edges(nodes_df, graph_df))

    graph = nx.DiGraph()

    def safe_str(value, default=""):
        if value is None:
            return default
        if isinstance(value, float) and math.isnan(value):
            return default
        text = str(value).strip()
        if text == "" or text.lower() == "nan":
            return default
        return text

    def safe_int(value, default=0):
        if value is None:
            return default
        if isinstance(value, float) and math.isnan(value):
            return default
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    for _, row in nodes_df.iterrows():
        node_id = row["node_id"]
        node_type = safe_str(row.get("node_type", "atomic_skill"), "atomic_skill")
        depth = safe_int(row.get("depth", 0), 0)
        area = safe_str(row.get("area", ""), "")
        level_band = safe_str(row.get("level_band", ""), "")
        title = safe_str(row.get("title", node_id), node_id)
        sort_order = safe_int(row.get("sort_order", 0), 0)
        parent_id = safe_str(row.get("parent_id", ""), "")

        if not title:
            title = str(node_id)

        if mastery_dict is None:
            mastery = 0.2 if node_type == "atomic_skill" else 0.5
        else:
            mastery = float(mastery_dict.get(node_id, 0.2))

        graph.add_node(
            node_id,
            label=title,
            group=area or level_band or "Unknown",
            level=depth,
            mastery=mastery,
            node_type=node_type,
            depth=depth,
            sort_order=sort_order,
            parent_id=parent_id,
            level_band=level_band,
            area=area,
        )

        if parent_id:
            graph.add_edge(
                parent_id,
                node_id,
                weight=1.0,
                edge_type="contains",
            )

    for _, row in graph_df.iterrows():
        node_id = row.get("node_id")
        prerequisites = row.get("prerequisite_ids")

        if not node_id:
            continue

        if node_id not in graph.nodes:
            mastery = float(mastery_dict.get(node_id, 0.2)) if mastery_dict else 0.2
            graph.add_node(
                node_id,
                label=str(node_id),
                group="",
                level=0,
                mastery=mastery,
                node_type="atomic_skill",
                depth=0,
                sort_order=0,
                parent_id="",
                level_band="",
                area="",
            )

        if not isinstance(prerequisites, str) or prerequisites.strip() == "":
            continue

        for prerequisite in prerequisites.split("|"):
            prereq_id = prerequisite.strip()
            if not prereq_id:
                continue

            if prereq_id not in graph.nodes:
                mastery = float(mastery_dict.get(prereq_id, 0.2)) if mastery_dict else 0.2
                graph.add_node(
                    prereq_id,
                    label=str(prereq_id),
                    group="",
                    level=0,
                    mastery=mastery,
                    node_type="atomic_skill",
                    depth=0,
                    sort_order=0,
                    parent_id="",
                    level_band="",
                    area="",
                )

            graph.add_edge(
                prereq_id,
                node_id,
                weight=1.0,
                edge_type="prereq",
            )

    # ── Inject augmented prerequisite edges ───────────────────────────────
    for (src, tgt), attrs in _EXTRA_PREREQ_EDGES.items():
        if src in graph.nodes and tgt in graph.nodes:
            if not graph.has_edge(src, tgt):
                graph.add_edge(src, tgt, **attrs)

    return graph


def calculate_pagerank(graph, edge_type=None):
    """Compute PageRank scores for every node in *graph*.

    PageRank (Brin & Page, 1998) was originally designed to rank web pages by
    counting incoming links.  In this curriculum graph the same idea measures
    **structural importance**: a skill that many other skills point *to* as a
    prerequisite receives a high score, meaning it is foundational for a large
    part of the curriculum.

    Why PageRank and not simple in-degree?
    ---------------------------------------
    PageRank is recursive: a skill gains importance not just from the *number*
    of skills that list it as a prerequisite, but from how important *those*
    skills are.  A single high-importance prerequisite contributes more than
    many low-importance ones.  This makes the ranking more semantically
    meaningful — core foundational skills bubble to the top.

    Edge-type filtering (``edge_type="prereq"``)
    --------------------------------------------
    The curriculum graph contains two kinds of edges:
      • "prereq"   — A is a prerequisite for B (the learning dependency)
      • "contains" — a topic node contains an atomic skill (hierarchy)

    Computing PageRank on *all* edges would let the hierarchy structure
    inflate scores for topic nodes.  When ``edge_type="prereq"`` is passed,
    only prerequisite edges are used, so the scores reflect pure learning
    dependencies and are directly comparable across atomic skills.

    If the filtered graph has no edges (e.g. all skills are roots), we fall
    back to the full graph to avoid returning a uniform trivial distribution.

    Edge weights
    ------------
    Same-area augmented edges carry weight 0.6; cross-area augmented edges
    carry weight 0.3; explicit curriculum prereq edges carry weight 1.0.
    networkx.pagerank uses these weights to scale the random-walk transition
    probabilities, so skills connected by strong same-area edges propagate
    more importance to their successors.

    Returns
    -------
    dict mapping node_id → float PageRank score.  Scores sum to 1.0 across
    all nodes.  In the UI these are normalised to percentiles for display.
    """
    if edge_type is None:
        return nx.pagerank(graph, weight="weight")

    # Build a subgraph containing only the requested edge type.
    # All nodes are retained so every skill receives a score.
    filtered = nx.DiGraph()
    for node, data in graph.nodes(data=True):
        filtered.add_node(node, **data)

    for source, target, data in graph.edges(data=True):
        if data.get("edge_type") == edge_type:
            filtered.add_edge(source, target, **data)

    # Guard: if no edges survive the filter, fall back to full graph PageRank
    # rather than returning a meaningless uniform distribution.
    if filtered.number_of_edges() == 0:
        return nx.pagerank(graph, weight="weight")

    return nx.pagerank(filtered, weight="weight")


def get_node_colors(graph):
    colors = []

    for node in graph.nodes:
        mastery = graph.nodes[node]["mastery"]

        if mastery < 0.4:
            colors.append("#E57373")
        elif mastery < 0.7:
            colors.append("#FFD54F")
        else:
            colors.append("#81C784")

    return colors


def get_node_sizes(graph, pagerank_scores):
    sizes = []

    for node in graph.nodes:
        size = 250 + pagerank_scores[node] * 2500
        sizes.append(size)

    return sizes


def get_layered_layout(graph=None):
    if graph is None:
        return {}

    positions = {}

    group_counts = {}

    for node in graph.nodes:
        group = graph.nodes[node]["group"]
        level = graph.nodes[node]["level"]

        group_counts.setdefault((group, level), 0)
        offset = group_counts[(group, level)]
        group_counts[(group, level)] += 1

        x = level * 1.35
        base_y = GROUP_ORDER.get(group, 0)

        y = base_y - offset * 0.55

        positions[node] = (x, y)

    return positions


def get_skill_status(mastery):
    if mastery < 0.4:
        return "Weak"
    if mastery < 0.7:
        return "Partial"
    return "Strong"


def get_prerequisite_subgraph(graph, target_skill):
    ancestors = nx.ancestors(graph, target_skill)
    nodes = ancestors | {target_skill}
    return graph.subgraph(nodes).copy()


def get_direct_prerequisites(graph, target_skill):
    return list(graph.predecessors(target_skill))


def get_all_prerequisites(graph, target_skill):
    return list(nx.ancestors(graph, target_skill))


def calculate_review_recommendations(graph, target_skill, pagerank_scores):
    recommendations = []

    prerequisites = [
        s for s in get_all_prerequisites(graph, target_skill)
        if graph.nodes[s].get("node_type") == "atomic_skill"
    ]

    for skill in prerequisites:
        mastery = graph.nodes[skill]["mastery"]
        importance = pagerank_scores[skill]

        try:
            distance = nx.shortest_path_length(graph, skill, target_skill)
        except nx.NetworkXNoPath:
            distance = 999

        distance_factor = 1 / distance
        priority = (1 - mastery) * importance * distance_factor

        recommendations.append({
            "skill_id": skill,
            "skill_name": graph.nodes[skill]["label"],
            "mastery": mastery,
            "importance": importance,
            "distance_to_target": distance,
            "priority": priority,
        })

    recommendations = sorted(
        recommendations,
        key=lambda item: item["priority"],
        reverse=True,
    )

    return recommendations


def get_top_recommended_skill(graph, target_skill, pagerank_scores):
    recommendations = calculate_review_recommendations(
        graph,
        target_skill,
        pagerank_scores,
    )

    if not recommendations:
        return target_skill

    return recommendations[0]["skill_id"]


def get_focused_prerequisite_graph(graph, target_skill, max_distance=4):
    ancestors = nx.ancestors(graph, target_skill)

    selected_nodes = {target_skill}

    for node in ancestors:
        try:
            distance = nx.shortest_path_length(graph, node, target_skill)
        except nx.NetworkXNoPath:
            continue

        if distance <= max_distance:
            selected_nodes.add(node)

    subgraph = graph.subgraph(selected_nodes).copy()

    if nx.is_directed_acyclic_graph(subgraph):
        reduced_edges = nx.transitive_reduction(subgraph).edges()

        clean_graph = nx.DiGraph()

        for node, data in subgraph.nodes(data=True):
            clean_graph.add_node(node, **data)

        for source, target in reduced_edges:
            clean_graph.add_edge(
                source,
                target,
                **subgraph.edges[source, target],
            )

        return clean_graph

    return subgraph
