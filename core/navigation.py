import networkx as nx

from core.skill_graph import LEVEL_BAND_ORDER


def build_learning_route(graph, target_skill, pagerank_scores, threshold):
    """Build a route: [most foundational unmastered prereq, …, target_skill].

    Strategy
    --------
    1. Walk the prereq graph to find every unmastered atomic ancestor of
       *target_skill* — these are skills the student needs but hasn't mastered.
    2. Take the top-12 by PageRank (most structurally important first) so the
       route stays at a manageable length even for deeply nested topics.
    3. Sort foundational-first: by level_band index, then by PageRank descending
       within each band.  This guarantees the student always works bottom-up.
    4. Append *target_skill* at the end.

    Result: a path of ≤ 13 skills, foundational → goal.  If all prerequisites
    are already mastered the route collapses to just [target_skill].
    """
    # Build prereq-only view for ancestor discovery
    prereq_only = nx.DiGraph()
    for u, v, data in graph.edges(data=True):
        if data.get("edge_type") == "prereq":
            prereq_only.add_edge(u, v)

    ancestors = (
        nx.ancestors(prereq_only, target_skill)
        if target_skill in prereq_only
        else set()
    )

    unmastered = [
        n for n in ancestors
        if (graph.nodes.get(n, {}).get("node_type") == "atomic_skill"
            and graph.nodes[n].get("mastery", 1.0) < threshold)
    ]

    if not unmastered:
        return [target_skill]

    # Keep the 12 most important (by PageRank) prerequisites
    top = sorted(unmastered, key=lambda n: pagerank_scores.get(n, 0), reverse=True)[:12]

    # Order foundational-first: earlier band → lower sort index
    def sort_key(n):
        lb = graph.nodes[n].get("level_band", "")
        band_idx = (
            LEVEL_BAND_ORDER.index(lb)
            if lb in LEVEL_BAND_ORDER
            else len(LEVEL_BAND_ORDER)
        )
        return (band_idx, -pagerank_scores.get(n, 0))

    top.sort(key=sort_key)
    top.append(target_skill)
    return top


def choose_next_after_attempt(
    graph,
    active_skill,
    target_skill,
    result_label,
    pagerank_scores,
    local_mastery_threshold,
    current_route,
    exclude_ids=None,
):
    """Decide the next skill to practice using pure route-based navigation.

    The route is treated as a spine from foundations to goal.  Navigation
    never leaves the route — it only moves one step forward or backward:

    Wrong / I don't know  →  step back one position (towards prerequisites).
                              If already at route[0], stay and keep drilling.
    Correct / Partial
      mastery < threshold  →  stay on current skill (need more practice).
      mastery ≥ threshold  →  step forward (one closer to the goal).

    This design guarantees:
    • The student always makes visible progress toward target_skill.
    • No infinite regression into arbitrary deep ancestors.
    • Backtracking is bounded: one step per wrong answer.

    Returns
    -------
    (next_skill_id, updated_route, reason_string)
    """
    active_mastery = graph.nodes[active_skill].get("mastery", 0.2)

    # Re-anchor if active_skill somehow fell outside the current route
    if active_skill not in current_route:
        current_route = build_learning_route(
            graph, target_skill, pagerank_scores, local_mastery_threshold
        )
        if active_skill not in current_route:
            # Prepend so the student can advance from here
            current_route = [active_skill] + current_route

    active_index = current_route.index(active_skill)

    # ── Wrong / I don't know — step backward ─────────────────────────────
    if result_label in ("I don't know", "Wrong"):
        if active_index > 0:
            next_skill = current_route[active_index - 1]
            reason = "reviewing a prerequisite to build a stronger foundation"
        else:
            next_skill = active_skill
            reason = "keep practicing — this is the most foundational skill on your path"
        return next_skill, current_route, reason

    # ── Correct / Partial — stay or step forward ──────────────────────────
    if active_mastery < local_mastery_threshold:
        return active_skill, current_route, "keep practicing to strengthen this skill"

    if active_index < len(current_route) - 1:
        next_skill = current_route[active_index + 1]
        return next_skill, current_route, "moving one step closer to the goal"

    return active_skill, current_route, "🎯 goal reached!"
