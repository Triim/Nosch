"""Content-based skill recommendation engine.

Algorithm
---------
After a student practices skill A, we score every other unmastered atomic
skill B in the graph with:

    Score(B | A) =
        0.40 * jaccard_ancestors(A, B)       # shared prerequisites → related topics
      + 0.25 * area_affinity(A, B)            # same / adjacent area bonus
      + 0.20 * level_score(A, B)              # prefer skills one level ahead
      + 0.10 * clip(0.6 - mastery(B), 0, 1)  # prefer skills in learning zone
      + 0.05 * normalized_pagerank(B)         # prefer structurally important skills

Components
~~~~~~~~~~
``jaccard_ancestors(A, B)``
    |anc(A) ∩ anc(B)| / max(1, |anc(A) ∪ anc(B)|).
    Ancestors are computed on ``prereq`` edges only (``contains`` edges are
    excluded).  A high Jaccard score means A and B share many prerequisite
    topics, indicating they are closely related in the curriculum.

``area_affinity(A, B)``
    1.0  if A and B share the same ``area``.
    0.4  if A and B are in adjacent level bands (|band_idx(A) - band_idx(B)| == 1).
    0.0  otherwise.

``level_score(A, B)``
    1.0  if B is in the same level band as A.
    0.8  if B is exactly one level band above A.
    0.4  if B is exactly two level bands above A.
    0.0  if B is lower or more than two bands higher.

``clip(0.6 - mastery(B), 0, 1)``
    Peaks when mastery(B) ≈ 0.2 (easy wins) and drops to zero when mastery
    ≥ 0.6 (skill is already fairly comfortable).

``normalized_pagerank(B)``
    pagerank(B) normalised to [0, 1] across all atomic skills.

Filter
~~~~~~
- Skills with mastery ≥ 0.75 are excluded (already mastered).
- Skill A itself is excluded.
- Only ``atomic_skill`` nodes are considered.

Caching
~~~~~~~
Ancestor sets are expensive to compute for large graphs.  We build them once
for all atomic skills on the first call and store them in the module-level
``_ancestor_cache`` dict.  The cache is keyed by node_id.  It is invalidated
(and rebuilt) when the set of nodes in the graph changes — detected by
comparing the frozenset of node IDs against ``_cache_graph_signature``.
"""

from __future__ import annotations

import networkx as nx

# ---------------------------------------------------------------------------
# Module-level ancestor cache.
# _ancestor_cache: {node_id: frozenset of ancestor node_ids (prereq only)}
# _cache_graph_signature: frozenset of node IDs seen when the cache was built.
# ---------------------------------------------------------------------------
_ancestor_cache: dict[str, frozenset] = {}
_cache_graph_signature: frozenset = frozenset()

LEVEL_BAND_ORDER = [
    "foundation",
    "school_algebra",
    "transition_to_university",
    "undergraduate_core",
    "advanced_undergraduate",
]


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _prereq_only_graph(graph: nx.DiGraph) -> nx.DiGraph:
    """Return a subgraph that contains only ``prereq``-type edges."""
    prereq_g = nx.DiGraph()
    for node, data in graph.nodes(data=True):
        prereq_g.add_node(node, **data)
    for u, v, data in graph.edges(data=True):
        if data.get("edge_type") == "prereq":
            prereq_g.add_edge(u, v, **data)
    return prereq_g


def _build_ancestor_cache(graph: nx.DiGraph) -> None:
    """Populate ``_ancestor_cache`` for every atomic skill in *graph*."""
    global _ancestor_cache, _cache_graph_signature

    prereq_g = _prereq_only_graph(graph)

    new_cache: dict[str, frozenset] = {}
    for node, data in graph.nodes(data=True):
        if data.get("node_type") == "atomic_skill":
            if node in prereq_g:
                new_cache[node] = frozenset(nx.ancestors(prereq_g, node))
            else:
                new_cache[node] = frozenset()

    _ancestor_cache = new_cache
    _cache_graph_signature = frozenset(graph.nodes())


def _ensure_cache(graph: nx.DiGraph) -> None:
    """Rebuild the ancestor cache if the graph has changed."""
    global _cache_graph_signature
    current_sig = frozenset(graph.nodes())
    if current_sig != _cache_graph_signature:
        _build_ancestor_cache(graph)


def _jaccard_ancestors(node_a: str, node_b: str) -> float:
    """Jaccard similarity of the prereq-ancestor sets of two nodes."""
    anc_a = _ancestor_cache.get(node_a, frozenset())
    anc_b = _ancestor_cache.get(node_b, frozenset())
    intersection = len(anc_a & anc_b)
    union = len(anc_a | anc_b)
    return intersection / max(1, union)


def _area_affinity(graph: nx.DiGraph, node_a: str, node_b: str) -> float:
    """Return 1.0 for same area, 0.4 for adjacent level band, 0.0 otherwise."""
    data_a = graph.nodes[node_a]
    data_b = graph.nodes[node_b]

    area_a = data_a.get("area", "")
    area_b = data_b.get("area", "")
    if area_a and area_b and area_a == area_b:
        return 1.0

    band_a = data_a.get("level_band", "")
    band_b = data_b.get("level_band", "")
    try:
        idx_a = LEVEL_BAND_ORDER.index(band_a)
        idx_b = LEVEL_BAND_ORDER.index(band_b)
    except ValueError:
        return 0.0

    if abs(idx_a - idx_b) == 1:
        return 0.4

    return 0.0


def _level_score(graph: nx.DiGraph, node_a: str, node_b: str) -> float:
    """Score based on level band difference (prefer B one step above A)."""
    band_a = graph.nodes[node_a].get("level_band", "")
    band_b = graph.nodes[node_b].get("level_band", "")
    try:
        idx_a = LEVEL_BAND_ORDER.index(band_a)
        idx_b = LEVEL_BAND_ORDER.index(band_b)
    except ValueError:
        return 0.0

    delta = idx_b - idx_a
    if delta == 0:
        return 1.0
    if delta == 1:
        return 0.8
    if delta == 2:
        return 0.4
    return 0.0


def _mastery_zone_score(mastery: float) -> float:
    """Return how much the skill sits in the 'learning zone' (mastery 0.2–0.6)."""
    return max(0.0, 0.6 - mastery)


def _build_reason(
    graph: nx.DiGraph,
    node_a: str,
    node_b: str,
    jaccard: float,
    area_aff: float,
    lvl_sc: float,
) -> str:
    """Produce a short human-readable explanation for the recommendation."""
    shared_count = len(
        _ancestor_cache.get(node_a, frozenset()) & _ancestor_cache.get(node_b, frozenset())
    )
    label_b = graph.nodes[node_b].get("label", node_b)
    area_b = graph.nodes[node_b].get("area", "")
    band_a = graph.nodes[node_a].get("level_band", "")
    band_b = graph.nodes[node_b].get("level_band", "")

    try:
        idx_a = LEVEL_BAND_ORDER.index(band_a)
        idx_b = LEVEL_BAND_ORDER.index(band_b)
        delta = idx_b - idx_a
    except ValueError:
        delta = 0

    if area_aff == 1.0:
        area_label = area_b or "the same area"
        if delta == 1:
            return f"next step in {area_label}"
        if delta == 0:
            return f"related skill in {area_label}"
        return f"complements your work in {area_label}"

    if shared_count >= 3:
        return f"shares {shared_count} prerequisites with this skill"
    if shared_count >= 1:
        return f"shares {shared_count} prerequisite{'s' if shared_count > 1 else ''} with this skill"
    if lvl_sc == 0.8:
        return "builds naturally on what you just practised"
    if lvl_sc == 1.0:
        return "at the same level — good for consolidation"

    return "expands your current knowledge"


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def recommend_related_skills(
    graph: nx.DiGraph,
    skill_id: str,
    mastery_dict: dict,
    pagerank_scores: dict,
    top_n: int = 3,
) -> list[dict]:
    """Return up to *top_n* recommended skills to practice after *skill_id*.

    Parameters
    ----------
    graph:
        The curriculum DiGraph produced by ``build_curriculum_graph``.
    skill_id:
        The node ID of the skill the student just practiced.
    mastery_dict:
        Mapping ``{node_id: float}`` of current mastery levels.
    pagerank_scores:
        Mapping ``{node_id: float}`` of pre-computed PageRank scores.
    top_n:
        Maximum number of results to return (default 3).

    Returns
    -------
    A list of dicts, each with keys::

        {
            "skill_id":   str,
            "skill_name": str,
            "score":      float,   # combined recommendation score in [0, 1]
            "reason":     str,     # short human-readable explanation
        }

    Sorted by ``score`` descending.
    """
    # Ensure the ancestor cache is up-to-date.
    _ensure_cache(graph)

    if skill_id not in graph.nodes:
        return []

    # Pre-compute normalised PageRank over atomic skills only.
    atomic_nodes = [
        n for n, d in graph.nodes(data=True)
        if d.get("node_type") == "atomic_skill"
    ]
    if not atomic_nodes:
        return []

    pr_values = [pagerank_scores.get(n, 0.0) for n in atomic_nodes]
    pr_max = max(pr_values) if pr_values else 1.0
    pr_min = min(pr_values) if pr_values else 0.0
    pr_range = pr_max - pr_min if pr_max != pr_min else 1.0

    def norm_pr(node: str) -> float:
        return (pagerank_scores.get(node, 0.0) - pr_min) / pr_range

    results = []

    for candidate in atomic_nodes:
        if candidate == skill_id:
            continue

        mastery = mastery_dict.get(candidate, graph.nodes[candidate].get("mastery", 0.2))

        # Skip already mastered skills.
        if mastery >= 0.75:
            continue

        jaccard = _jaccard_ancestors(skill_id, candidate)
        area_aff = _area_affinity(graph, skill_id, candidate)
        lvl_sc = _level_score(graph, skill_id, candidate)
        mastery_zone = _mastery_zone_score(mastery)
        npr = norm_pr(candidate)

        score = (
            0.40 * jaccard
            + 0.25 * area_aff
            + 0.20 * lvl_sc
            + 0.10 * mastery_zone
            + 0.05 * npr
        )

        if score <= 0.0:
            continue

        reason = _build_reason(graph, skill_id, candidate, jaccard, area_aff, lvl_sc)

        results.append({
            "skill_id": candidate,
            "skill_name": graph.nodes[candidate].get("label", candidate),
            "score": round(score, 4),
            "reason": reason,
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_n]
