from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to call this API

# Configure Gemini API
# Replace with your actual API key from https://aistudio.google.com/app/apikey
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyARV2aBhqCdHmmGfXrJSJS6LN3R-GXWdfc")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "CareerBridge API is running!"})


@app.route("/api/recommend", methods=["POST"])
def recommend():
    """Main endpoint: takes student profile, returns career + scholarship recommendations"""
    data = request.json

    # Extract student info from request
    name = data.get("name", "Student")
    stream = data.get("stream", "")
    grades = data.get("grades", "")
    state = data.get("state", "")
    income = data.get("income", "")
    interests = data.get("interests", "")
    goal = data.get("goal", "")

    # Build a detailed prompt for Gemini
    prompt = f"""
You are CareerBridge, an AI career and scholarship advisor for Indian students.

A student has provided the following details:
- Name: {name}
- Stream/Class: {stream}
- Grades/Percentage: {grades}
- State: {state}
- Family Annual Income: {income}
- Interests: {interests}
- Career Goal: {goal}

Please provide a comprehensive, personalized response in the following EXACT format:

## CAREER PATHS
Suggest 3 career paths that best match this student's profile. For each:
1. [Career Name]: [2-3 sentences about what it is, why it suits this student, and what skills are needed]
2. [Career Name]: [description]
3. [Career Name]: [description]

## SCHOLARSHIPS & SCHEMES
List 5 government scholarships or schemes this student likely qualifies for. For each:
1. [Scholarship Name] - [Eligibility in one line] - Apply at: [website/portal]
2. [repeat format]
3. [repeat]
4. [repeat]
5. [repeat]

## HOW TO APPLY
Give a 5-step actionable guide to apply for the most relevant scholarship:
Step 1: [action]
Step 2: [action]
Step 3: [action]
Step 4: [action]
Step 5: [action]

## NEXT STEPS
Give 3 immediate actionable next steps this student should take this week.

Keep the language simple, encouraging, and easy to understand for a student who may be first-generation.
"""

    try:
        response = model.generate_content(prompt)
        return jsonify({
            "success": True,
            "result": response.text
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route("/api/chat", methods=["POST"])
def chat():
    """Chat endpoint for follow-up questions"""
    data = request.json
    message = data.get("message", "")
    history = data.get("history", [])  # List of {role, text} objects

    # Build conversation context
    chat_prompt = """You are CareerBridge, a friendly AI career advisor for Indian students. 
You help students with career guidance, scholarships, government schemes, entrance exams, and education decisions.
Keep your answers concise, simple, and encouraging. Use examples relevant to India."""

    # Build message history for context
    full_prompt = chat_prompt + "\n\n"
    for msg in history[-6:]:  # Last 6 messages for context
        role = "Student" if msg["role"] == "user" else "CareerBridge"
        full_prompt += f"{role}: {msg['text']}\n"
    full_prompt += f"Student: {message}\nCareerBridge:"

    try:
        response = model.generate_content(full_prompt)
        return jsonify({
            "success": True,
            "reply": response.text
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
