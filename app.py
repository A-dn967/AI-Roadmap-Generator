
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🧠",
    layout="centered"
)

# Application title
st.title("🧠 AI Learning Roadmap Generator")

st.write(
    "Create a personalized learning roadmap "
    "based on your goals, skill level, and available time."
)

st.divider()

# User input section
st.subheader("Your Learning Preferences")

# Learning field
field = st.text_input(
    "What do you want to learn?",
    placeholder="e.g. Cybersecurity, Python, AI"
)

# Skill level
level = st.selectbox(
    "Select your current skill level",
    ["Beginner", "Intermediate", "Advanced"]
)

# Learning duration
duration = st.selectbox(
    "How much time do you have?",
    ["1 month", "3 months", "6 months", "1 year"]
)

# Generate button
if st.button("🚀 Generate My Roadmap"):

    if field.strip():
        st.success("Your inputs have been received!")

        st.write("**Learning Field:**", field)
        st.write("**Skill Level:**", level)
        st.write("**Available Time:**", duration)

    else:
        st.warning("Please enter a learning field.")
