import random

# Mastery range per level band per profile
_LEVEL_RANGES = {
    "foundation": {
        "alina": (0.82, 0.96),
        "artem": (0.58, 0.76),
        "ilya":  (0.22, 0.44),
    },
    "school_algebra": {
        "alina": (0.72, 0.90),
        "artem": (0.42, 0.63),
        "ilya":  (0.14, 0.30),
    },
    "transition_to_university": {
        "alina": (0.58, 0.78),
        "artem": (0.28, 0.50),
        "ilya":  (0.10, 0.22),
    },
    "undergraduate_core": {
        "alina": (0.48, 0.68),
        "artem": (0.18, 0.40),
        "ilya":  (0.10, 0.18),
    },
    "advanced_undergraduate": {
        "alina": (0.32, 0.56),
        "artem": (0.10, 0.26),
        "ilya":  (0.10, 0.14),
    },
}

PROFILE_META = {
    "default": {"name": "New Student", "emoji": "👤", "desc": "No history"},
    "alina":   {"name": "Alina",       "emoji": "⭐", "desc": "Advanced student"},
    "artem":   {"name": "Artem",       "emoji": "📚", "desc": "Average student"},
    "ilya":    {"name": "Ilya",        "emoji": "📖", "desc": "Beginner student"},
}

_SEEDS = {"alina": 101, "artem": 202, "ilya": 303}


def _result_pool(profile_name):
    return {
        "alina": ["Correct"] * 7 + ["Wrong"] * 2 + ["I don't know"] * 1,
        "artem": ["Correct"] * 5 + ["Wrong"] * 3 + ["I don't know"] * 2,
        "ilya":  ["Correct"] * 2 + ["Wrong"] * 4 + ["I don't know"] * 4,
    }.get(profile_name, ["Correct"] * 5 + ["Wrong"] * 5)


def _gen_mastery(nodes_df, profile_name, rng):
    mastery = {}
    for _, row in nodes_df.iterrows():
        node_id = row["node_id"]
        node_type = str(row.get("node_type", "")).strip()
        level_band = str(row.get("level_band", "")).strip()
        if node_type == "atomic_skill":
            lo, hi = _LEVEL_RANGES.get(level_band, {}).get(profile_name, (0.2, 0.2))
            mastery[node_id] = round(rng.uniform(lo, hi), 3)
        else:
            mastery[node_id] = 0.5
    return mastery


def _gen_practice_log(nodes_df, mastery_dict, profile_name, rng):
    """Generate a practice log that supports linear regression time estimates.
    Per-skill entries are in chronological order (increasing mastery) so
    mastery_history_for() returns a monotone sequence suitable for polyfit.
    """
    pool = _result_pool(profile_name)
    log = []

    for _, row in nodes_df.iterrows():
        node_id = row["node_id"]
        if str(row.get("node_type", "")).strip() != "atomic_skill":
            continue

        title = str(row.get("title", node_id))
        current = mastery_dict.get(node_id, 0.2)

        # Number of practice sessions based on final mastery
        if current < 0.25:
            n = rng.choice([0, 0, 1])
        elif current < 0.45:
            n = rng.randint(2, 4)
        elif current < 0.65:
            n = rng.randint(4, 6)
        else:
            n = rng.randint(5, 8)

        if n == 0:
            continue

        # Build trajectory from ~0.2 up to current mastery
        start = max(0.10, current - n * 0.10)
        step = (current - start) / n

        prev = start
        for i in range(n):
            before = round(prev + rng.uniform(-0.015, 0.015), 3)
            before = max(0.10, min(0.99, before))
            result = rng.choice(pool)
            if result == "Correct":
                after = min(1.0, before + rng.uniform(0.08, 0.15))
            elif result == "Wrong":
                after = min(1.0, before + rng.uniform(0.01, 0.06))
            else:
                after = max(0.10, before - rng.uniform(0.00, 0.03))
            after = round(after, 3)
            log.append({
                "skill_id":   node_id,
                "skill_name": title,
                "result":     result,
                "before":     before,
                "after":      after,
                "task":       "Practice task",
            })
            prev = start + step * (i + 1)

    return log


def load_profile(profile_key, nodes_df):
    """Return (mastery_dict, practice_log) for the given profile key."""
    if profile_key == "default":
        mastery = {
            row["node_id"]: (0.2 if str(row.get("node_type", "")).strip() == "atomic_skill" else 0.5)
            for _, row in nodes_df.iterrows()
        }
        return mastery, []

    seed = _SEEDS.get(profile_key, 42)
    rng = random.Random(seed)
    mastery = _gen_mastery(nodes_df, profile_key, rng)
    log = _gen_practice_log(nodes_df, mastery, profile_key, rng)
    return mastery, log
