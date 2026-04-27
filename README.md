# CareerBridge 🎓
### AI-Powered Career Guidance & Scholarship Advisor for Indian Students

Built with Google Gemini AI | Solution Challenge 2026

---

## What it does
Students enter their stream, grades, state, income, and interests → AI instantly gives:
- **Personalized career path recommendations**
- **Government scholarships and schemes they qualify for**
- **Step-by-step application guidance**
- **AI chatbot for follow-up questions**

---

## ⚡ QUICK START (Get it running in 15 minutes)

### Step 1: Get your FREE Gemini API Key
1. Go to: https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key (looks like: `AIzaSy...`)

### Step 2: Set up Backend

```bash
# Go to backend folder
cd backend/

# Install Python packages
pip install -r requirements.txt

# Set your API key (replace with your actual key)
# On Mac/Linux:
export GEMINI_API_KEY="AIzaSy_your_key_here"

# On Windows (Command Prompt):
set GEMINI_API_KEY=AIzaSy_your_key_here

# Run the server
python app.py
```

You should see: `Running on http://0.0.0.0:5000`

### Step 3: Open the Frontend

Simply open `frontend/index.html` in your browser.
- Double-click the file, OR
- Drag it into Chrome/Firefox

The app should be working now! Try entering your details and clicking "Get My Recommendations".

---

## 🚀 DEPLOYMENT (For Submission)

You need a live URL for submission. Here's the FREE way:

### Deploy Backend to Google Cloud Run

```bash
# 1. Install Google Cloud CLI: https://cloud.google.com/sdk/docs/install

# 2. Login
gcloud auth login

# 3. Create a project (or use existing)
gcloud projects create careerbridge-2026 --name="CareerBridge"
gcloud config set project careerbridge-2026

# 4. Enable required APIs
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com

# 5. Deploy from backend folder
cd backend/
gcloud run deploy careerbridge-api \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --set-env-vars GEMINI_API_KEY=your_actual_key_here

# 6. Copy the URL it gives you (like: https://careerbridge-api-xxx-uc.a.run.app)
```

### Deploy Frontend to Firebase Hosting

```bash
# 1. Install Firebase CLI
npm install -g firebase-tools

# 2. Login
firebase login

# 3. In the frontend/ folder:
cd frontend/

# 4. IMPORTANT: Edit index.html, change this line:
# const API_BASE = "http://localhost:5000";
# TO:
# const API_BASE = "https://your-cloud-run-url.run.app";

# 5. Initialize Firebase (select "Hosting", use current directory)
firebase init hosting

# 6. Deploy
firebase deploy --only hosting

# 7. Your app is live at: https://your-project-id.web.app
```

---

## Project Structure

```
careerbridge/
├── backend/
│   ├── app.py              # Flask API server (main backend)
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # For Cloud Run deployment
└── frontend/
    └── index.html          # Complete frontend (single file!)
```

## Tech Stack
- **AI**: Google Gemini 1.5 Flash API
- **Backend**: Python + Flask
- **Frontend**: HTML + CSS + JavaScript (no frameworks needed)
- **Hosting**: Firebase Hosting (frontend) + Google Cloud Run (backend)

## SDG Goals Addressed
- SDG 4: Quality Education
- SDG 10: Reduced Inequalities  
- SDG 8: Decent Work and Economic Growth
