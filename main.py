# main.py

import streamlit as st
from recommender import load_data, generate_workout
import pandas as pd
import ast
from PIL import Image
from pathlib import Path
from storage import save_workout, load_saved_workouts


# Load data
df = load_data()

st.title("💪 FitGenie - Smart Workout Planner")
st.markdown("Your free, personalised fitness assistant.")

# User inputs
force = st.selectbox("Choose a workout type:", ["push", "pull", "legs"])
level = st.selectbox("Choose difficulty:", df['level'].unique())
equipment = st.text_input("Available equipment (e.g. body only, dumbbell)", "")
goal = st.selectbox("🎯 What’s your current fitness goal?", [
    "Build muscle (Hypertrophy)",
    "Get stronger (Strength)",
    "Lose fat (Fat loss / Cardio)",
    "Stay active / Maintain fitness"
])

# Generate workout
if st.button("Generate Workout"):
    workout = generate_workout(df, force, 5, level, equipment, goal)
    save_workout(workout)
    st.success("Workout generated successfully!")

    for i, row in workout.iterrows():
        st.subheader(f"{i+1}. {row['name']}")
        st.markdown(f"**Primary Muscles:** {row['primaryMuscles']}")
        st.markdown(f"**Instructions:**")
        try:
            instructions = ast.literal_eval(row['instructions']) if isinstance(row['instructions'], str) else []
            for step in instructions:
                st.markdown(f"- {step}")
        except:
            st.warning("No instructions available.")

        # Display image if available
        try:
            image_list = ast.literal_eval(row['images']) if isinstance(row['images'], str) else []
            for img in image_list:
                image_path = Path("images") / img
                if image_path.exists():
                    st.image(str(image_path))
        except:
            pass

with st.expander("📚 View Past Workouts"):
    history = load_saved_workouts()
    if history:
        for session in reversed(history[-5:]):  # Show last 5 workouts
            st.markdown(f"**🕒 {session['timestamp']}**")
            for i, ex in enumerate(session["workout"]):
                st.markdown(f"- {i+1}. {ex['name']} ({ex.get('primaryMuscles', 'N/A')})")
            st.markdown("---")
    else:
        st.info("No past workouts found yet.")
