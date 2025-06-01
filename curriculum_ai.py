import streamlit as st
from typing import List, Dict, Any

# Mock curriculum database
CURRICULUM_DB = {
    "Introduction to Python": [
        "Introduction & Setup",
        "Variables and Data Types",
        "Input and Output",
        "Control Flow - if/else",
        "Loops - for/while",
        "Functions and Scope",
        "Data Structures - lists, tuples, dicts",
        "Modules and Packages",
        "File I/O",
        "Error Handling",
        "Basic Object-Oriented Programming",
        "Intro to Libraries - numpy, pandas"
    ],
    "Mathematics - Algebra": [
        "Arithmetic Operations",
        "Linear Equations",
        "Inequalities",
        "Graphs and Functions",
        "Polynomials",
        "Factoring",
        "Quadratic Equations",
        "Exponents and Radicals",
        "Word Problems"
    ]
}

def generate_curriculum(subject: str, duration_weeks: int, learner_profile: Dict[str, Any]) -> List[Dict[str, Any]]:
    topics = CURRICULUM_DB.get(subject, [])
    if not topics:
        return [{"error": f"Subject '{subject}' not found in curriculum database."}]

    topics_per_week = max(1, len(topics) // duration_weeks)
    curriculum = []

    for i in range(duration_weeks):
        start_idx = i * topics_per_week
        end_idx = start_idx + topics_per_week
        week_topics = topics[start_idx:end_idx]
        if week_topics:
            curriculum.append({
                "week": i + 1,
                "topics": week_topics
            })

    # Add remaining topics to the last week
    remaining = topics[duration_weeks * topics_per_week:]
    if remaining and curriculum:
        curriculum[-1]["topics"].extend(remaining)

    return curriculum

# Streamlit UI
st.title("📘 Curriculum AI Generator")

subject = st.selectbox("Select a subject", list(CURRICULUM_DB.keys()))
duration = st.slider("Course duration (weeks)", min_value=1, max_value=12, value=4)

st.subheader("Learner Profile")
age = st.number_input("Age", min_value=5, max_value=100, value=20)
level = st.selectbox("Skill Level", ["beginner", "intermediate", "advanced"])
goal = st.text_input("Learning Goal", "basic scripting & data handling")

if st.button("Generate Curriculum"):
    learner_profile = {"age": age, "level": level, "goal": goal}
    curriculum = generate_curriculum(subject, duration, learner_profile)

    if curriculum and "error" in curriculum[0]:
        st.error(curriculum[0]["error"])
    else:
        for week in curriculum:
            st.markdown(f"### Week {week['week']}")
            for topic in week["topics"]:
                st.markdown(f"- {topic}")