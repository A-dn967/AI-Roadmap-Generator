# 🧠 AI Learning Roadmap Generator

An AI-powered application that generates personalized learning roadmaps based on a user's chosen field, current skill level, and available learning time.

## 🚀 Overview

The AI Learning Roadmap Generator helps learners plan their learning journey in a structured and efficient way.

Users enter their learning preferences, and the application generates a customized roadmap with topics, practical exercises, projects, and learning milestones.

## ✨ Features

- 🎯 Personalized learning roadmaps
- 📚 Multiple learning fields
- 🧑‍💻 Beginner, Intermediate, and Advanced skill levels
- ⏳ Flexible learning durations
- 🤖 AI-powered roadmap generation using Groq
- 📥 Downloadable learning roadmaps
- 🌐 Simple and interactive Streamlit interface

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Google Colab | Development environment |
| Streamlit | User interface |
| Groq API | AI-powered roadmap generation |
| GitHub | Version control and project hosting |

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-learning-roadmap-generator.git
```

### 2. Navigate to the project directory

```bash
cd ai-learning-roadmap-generator
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Groq API key

Create a `.streamlit/secrets.toml` file and add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Get your API key from [Groq Console](https://console.groq.com/).

### 5. Run the application

```bash
streamlit run app.py
```

## 📖 How to Use

1. Enter the field you want to learn.
2. Select your current skill level.
3. Choose your available learning duration.
4. Click **Generate My Roadmap**.
5. Review your personalized roadmap.
6. Download your roadmap for future reference.

## 🎯 Example

**Input:**
- Learning Field: Cybersecurity
- Skill Level: Beginner
- Available Time: 6 Months

**Output:**

A structured six-month cybersecurity roadmap covering networking fundamentals, Linux, security concepts, ethical hacking basics, hands-on projects, and a final practical project.

## 🔐 Security

- Keep your Groq API key private.
- Never commit API keys or credentials to GitHub.
- Use Streamlit Secrets for deployment.

## 👨‍💻 Author

Adnan Khan

BS Cyber Security Student | Aspiring Cybersecurity Professional

## 📄 License

This project is intended for educational and learning purposes.
