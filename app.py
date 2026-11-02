
import streamlit as st
import os
from groq import Groq

# Page Configuration
st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🎯",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f8f9fc;
}
.roadmap-title {
    color: #4F46E5;
    text-align: center;
    font-size: 36px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown(
    '<div class="roadmap-title">🎯 AI Learning Roadmap Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Create your personalized AI-powered learning journey</div>',
    unsafe_allow_html=True
)

st.divider()

# Input Section
st.subheader("📚 Your Learning Preferences")

col1, col2 = st.columns(2)

with col1:
    learning_field = st.text_input(
        "What do you want to learn?",
        placeholder="e.g. Cyber Security, Python, AI"
    )

    skill_level = st.selectbox(
        "Select your current skill level",
        ["Beginner", "Intermediate", "Advanced"]
    )

with col2:
    duration = st.selectbox(
        "How much time do you have?",
        ["1 month", "2 months", "3 months",
         "6 months", "12 months"]
    )

    daily_hours = st.selectbox(
        "How much time can you study daily?",
        ["30 minutes", "1 hour", "2 hours",
         "3 hours", "4+ hours"]
    )

# Generate Button
generate = st.button(
    "🚀 Generate My Roadmap",
    type="primary",
    use_container_width=True
)

# API Key
try:
    API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    API_KEY = os.getenv("GROQ_API_KEY")

# Generate Roadmap
if generate:

    if not learning_field.strip():
        st.warning("Please enter a learning field.")

    elif not API_KEY:
        st.error(
            "Groq API key not found. "
            "Please add GROQ_API_KEY in Streamlit Secrets."
        )

    else:
        try:
            client = Groq(api_key=API_KEY)

            prompt = f"""
You are an expert learning roadmap designer and instructor.

Create a detailed, practical, personalized learning roadmap.

USER DETAILS:
Learning Field: {learning_field}
Current Skill Level: {skill_level}
Available Duration: {duration}
Daily Study Time: {daily_hours}

IMPORTANT INSTRUCTIONS:
1. Generate an actual learning roadmap, not a summary of user inputs.
2. Divide the roadmap into weeks according to the selected duration.
3. Include specific topics and subtopics for every week.
4. Include free learning resources with working URLs where possible.
5. Include hands-on exercises and practical labs.
6. Include weekly assignments and milestones.
7. Include at least one practical project.
8. Include a final project appropriate to the user's skill level.
9. Make the plan realistic for the available daily study time.
10. Use simple, beginner-friendly language where appropriate.
11. Use proper Markdown formatting.

OUTPUT FORMAT:

# 🎯 Your Personalized {learning_field} Roadmap

## 📌 Learning Overview
Explain what the learner will achieve.

## 🗓️ Complete Weekly Learning Plan

For every week, provide:
- Learning objectives
- Topics to study
- Recommended resources
- Practical exercises
- Weekly milestone

## 🛠️ Practical Projects
Suggest projects suitable for the learner's level.

## 📖 Recommended Free Resources
Provide useful websites, courses, documentation, and tools.

## 🎓 Final Capstone Project
Explain a project that demonstrates the learner's skills.

## ✅ Expected Outcomes
Explain what the learner should be able to do after completing the roadmap.

Generate the complete roadmap now.
"""

            with st.spinner(
                "🤖 AI is creating your personalized roadmap..."
            ):

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a professional AI learning "
                                "roadmap generator. Always generate "
                                "a complete and practical roadmap."
                            )
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.7,
                    max_tokens=8000
                )

                roadmap = response.choices[0].message.content

            # Display Actual AI Roadmap
            st.success("🎉 Your personalized roadmap is ready!")

            st.divider()

            st.markdown(roadmap)

            # Download Roadmap
            st.download_button(
                label="📥 Download Your Roadmap",
                data=roadmap,
                file_name="my_learning_roadmap.md",
                mime="text/markdown"
            )

        except Exception as e:
            st.error("Unable to generate roadmap.")
            st.error(f"Error details: {str(e)}")

# Footer
st.divider()

st.markdown(
    "<center>Built with ❤️ using Python, Streamlit & Groq AI</center>",
    unsafe_allow_html=True
)
