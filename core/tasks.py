import random
import re
from fractions import Fraction

import pandas as pd


DEFAULT_NUMERIC_TOLERANCE = 0.02


def load_tasks(path="data/tasks.csv"):
    return pd.read_csv(path)


def difficulty_from_mastery(mastery):
    if mastery < 0.4:
        return "easy"
    if mastery < 0.7:
        return "medium"
    return "hard"


def get_task_for_skill(tasks_df, skill_id, mastery=None, seed=None):
    matching = tasks_df[tasks_df["skill_id"] == skill_id]

    if matching.empty:
        return None

    rng = random.Random(seed) if seed is not None else random

    if mastery is None:
        return matching.iloc[rng.randrange(len(matching))].to_dict()

    difficulty = difficulty_from_mastery(mastery)
    difficulty_matching = matching[matching["difficulty"] == difficulty]

    if not difficulty_matching.empty:
        return difficulty_matching.iloc[rng.randrange(len(difficulty_matching))].to_dict()

    return matching.iloc[rng.randrange(len(matching))].to_dict()


def normalize_answer(answer):
    return (
        str(answer)
        .strip()
        .lower()
        .replace(" ", "")
    )


def try_parse_number(value):
    text = normalize_answer(value)

    text = text.replace(",", ".")

    if text.startswith("x="):
        text = text[2:]

    try:
        return float(Fraction(text))
    except Exception:
        pass

    try:
        return float(text)
    except Exception:
        return None


def extract_numbers(value):
    text = str(value)

    matches = re.findall(
        r"-?\d+(?:\.\d+)?(?:/\d+(?:\.\d+)?)?",
        text,
    )

    numbers = []

    for item in matches:
        parsed = try_parse_number(item)

        if parsed is not None:
            numbers.append(parsed)

    return numbers


def numeric_answers_close(user_answer, expected_answer, tolerance):
    user_number = try_parse_number(user_answer)
    expected_number = try_parse_number(expected_answer)

    if user_number is not None and expected_number is not None:
        return abs(user_number - expected_number) <= tolerance

    user_numbers = extract_numbers(user_answer)
    expected_numbers = extract_numbers(expected_answer)

    if not user_numbers or not expected_numbers:
        return False

    if len(user_numbers) != len(expected_numbers):
        return False

    for user_value, expected_value in zip(user_numbers, expected_numbers):
        if abs(user_value - expected_value) > tolerance:
            return False

    return True


def check_answer(user_answer, accepted_answers, tolerance=DEFAULT_NUMERIC_TOLERANCE):
    if user_answer is None or str(user_answer).strip() == "":
        return False

    if str(accepted_answers).strip() == "__any__":
        return True

    normalized_user = normalize_answer(user_answer)
    accepted = str(accepted_answers).split("|")

    for answer in accepted:
        if normalized_user == normalize_answer(answer):
            return True

    for answer in accepted:
        if numeric_answers_close(user_answer, answer, tolerance):
            return True

    return False
