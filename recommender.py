# recommender.py

import pandas as pd
import random


# Load exercise data from CSV
def load_data(path="clean_exercises.csv"):
    return pd.read_csv(path)


# Filter by workout type: push, pull, legs
# Add this near the top of recommender.py
GOAL_MAPPING = {
    "Build muscle (Hypertrophy)": ["compound", "isolation"],
    "Get stronger (Strength)": ["compound"],
    "Lose fat (Fat loss / Cardio)": ["cardio", "bodyweight"],
    "Stay active / Maintain fitness": ["light strength", "mobility", "stretching"]
}


def filter_by_force(df, force_type, level=None, equipment=None, goal=None):
    force_filtered = df[df['force'].str.lower() == force_type.lower()]

    if level:
        force_filtered = force_filtered[force_filtered['level'].str.lower() == level.lower()]

    if equipment:
        force_filtered = force_filtered[
            force_filtered['equipment'].fillna('').str.lower().str.contains(equipment.lower())
        ]

    print(f"\n--- Filtering for goal: {goal} ---")

    if goal:
        if goal in ["Lose fat (Fat loss / Cardio)", "Stay active / Maintain fitness"]:
            category_map = {
                "Lose fat (Fat loss / Cardio)": ["cardio", "plyometrics", "full body", "stretching"],
                "Stay active / Maintain fitness": ["stretching", "mobility", "light strength"]
            }
            target_categories = category_map.get(goal, [])
            print("Using categories:", target_categories)
            force_filtered = force_filtered[
                force_filtered['category'].fillna('').str.lower().isin([c.lower() for c in target_categories])
            ]
        else:
            GOAL_MAPPING = {
                "Build muscle (Hypertrophy)": ["compound", "isolation"],
                "Get stronger (Strength)": ["compound"]
            }
            mechanics = GOAL_MAPPING.get(goal, [])
            print("Using mechanics:", mechanics)
            force_filtered = force_filtered[
                force_filtered['mechanic'].fillna('').str.lower().isin([m.lower() for m in mechanics])
            ]

    print("Filtered rows:", len(force_filtered))
    return force_filtered


def generate_workout(df, force_type="push", num_exercises=5, level="beginner", equipment=None, goal=None):
    filtered = filter_by_force(df, force_type, level, equipment, goal)
    if len(filtered) < num_exercises:
        num_exercises = len(filtered)
    return filtered.sample(num_exercises).reset_index(drop=True)
