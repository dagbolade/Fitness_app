# storage.py

import json
from datetime import datetime
from pathlib import Path

SAVE_PATH = Path("saved_workouts.json")


def save_workout(workout_df):
    workout_history = load_saved_workouts()
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    workout = {
        "timestamp": today,
        "workout": workout_df.to_dict(orient="records")
    }

    workout_history.append(workout)
    with open(SAVE_PATH, "w") as f:
        json.dump(workout_history, f, indent=2)


def load_saved_workouts():
    if not SAVE_PATH.exists():
        return []
    with open(SAVE_PATH, "r") as f:
        return json.load(f)
