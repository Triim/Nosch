import math
import networkx as nx


def get_prerequisite_factor(graph, target_skill, min_factor=0.25):
    prerequisites = list(nx.ancestors(graph, target_skill))

    if not prerequisites:
        return 1.0

    values = []

    for skill in prerequisites:
        mastery = graph.nodes[skill].get("mastery", 0.2)

        try:
            distance = nx.shortest_path_length(graph, skill, target_skill)
        except nx.NetworkXNoPath:
            distance = 999

        weight = 1 / distance
        values.append((mastery, weight))

    weighted_sum = sum(mastery * weight for mastery, weight in values)
    total_weight = sum(weight for _, weight in values)

    factor = weighted_sum / total_weight

    return max(min_factor, factor)


def effective_learning_rate(base_rate, prerequisite_factor, difficulty):
    return base_rate * prerequisite_factor / difficulty


def mastery_after_sessions(initial_mastery, learning_rate, sessions):
    if sessions < 0:
        return initial_mastery

    return 1 - (1 - initial_mastery) * math.exp(-learning_rate * sessions)


def build_learning_curve(initial_mastery, learning_rate, max_sessions):
    curve = []

    for session in range(max_sessions + 1):
        mastery = mastery_after_sessions(
            initial_mastery,
            learning_rate,
            session,
        )

        curve.append({
            "session": session,
            "mastery": mastery,
        })

    return curve


def update_mastery_value(current_mastery, result_score, learning_gain):
    delta = learning_gain * result_score * (1 - current_mastery)
    new_mastery = current_mastery + delta

    return min(1.0, max(0.0, new_mastery))


def apply_practice_result(
    mastery_dict,
    graph,
    target_skill,
    result_score,
    learning_gain,
    prerequisite_gain,
):
    updated = mastery_dict.copy()

    current = updated.get(target_skill, 0.2)

    updated[target_skill] = update_mastery_value(
        current_mastery=current,
        result_score=result_score,
        learning_gain=learning_gain,
    )

    prerequisites = [
        s for s in nx.ancestors(graph, target_skill)
        if graph.nodes[s].get("node_type") == "atomic_skill"
    ]

    for skill in prerequisites:
        try:
            distance = nx.shortest_path_length(graph, skill, target_skill)
        except nx.NetworkXNoPath:
            continue

        influence = prerequisite_gain / distance

        updated[skill] = update_mastery_value(
            current_mastery=updated.get(skill, 0.2),
            result_score=result_score,
            learning_gain=influence,
        )

    return updated
