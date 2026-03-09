# 🤖 MathBot9 — Ontario Grade 9 Math Chatbot

A fun, interactive AI-powered math tutor for Ontario Grade 9 students (MTH1W).
Built with Python, Streamlit, and the Anthropic Claude API. Designed using Canva.

---

## ✨ Features

- 💬 Interactive AI chat powered by Claude (claude-opus-4-5)
- 📚 Aligned to Ontario MTH1W curriculum expectations
- 📋 Growing Success assessment language built into responses
- 🎯 6 curriculum strands with focused mode
- ⚡ Quick-start prompts for common topics
- 🔥 Streak tracking to motivate students
- 🎨 Futuristic dark-space UI matching the Canva branding

---

## 🚀 Quick Start (Local)

### 1. Clone the project
```bash
git clone https://github.com/your-username/mathbot9.git
cd mathbot9
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
```bash
cp .env.example .env
# Open .env and replace 'your_api_key_here' with your actual Anthropic API key
# Get a key at: https://console.anthropic.com
```

### 5. Run MathBot9
```bash
streamlit run app.py
```

Open http://localhost:8501 in your browser. You're live! 🎉

---

## 🌐 Deploy as a Website (Streamlit Community Cloud — FREE)

1. Push your code to a **public GitHub repository**
   - Make sure `.env` is in `.gitignore` (it is by default)
2. Go to **https://share.streamlit.io**
3. Sign in with GitHub
4. Click **"New app"** → select your repo → select `app.py`
5. Under **"Advanced settings"**, add your secret:
   - Key: `ANTHROPIC_API_KEY`
   - Value: `sk-ant-...` (your actual API key)
6. Click **Deploy** — you get a permanent shareable URL!

Share the URL with your students. Done! 🚀

---

## 📁 File Structure

```
mathbot9/
├── app.py              # Main Streamlit app (UI + chat logic)
├── bot_logic.py        # Anthropic API calls + error handling
├── curriculum.py       # Ontario MTH1W curriculum expectations
├── prompts.py          # MathBot9 system prompt builder
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Prevents secrets from being committed
└── .streamlit/
    └── config.toml     # Streamlit dark theme config
```

---

## 🔮 Future Expansion

This project is designed to scale. To add Grade 10 or new subjects:

1. Add new expectations to `curriculum.py` under a new grade key
2. Update `prompts.py` to accept a `grade` parameter
3. Add a grade selector dropdown in the `app.py` sidebar
4. Repeat for any subject!

---

## 📋 Curriculum Resources

- [Ontario Math Curriculum (MTH1W)](https://www.ontario.ca/document/mathematics-curriculum-grades-1-8-2020)
- [Growing Success: Assessment, Evaluation, and Reporting](https://www.ontario.ca/document/growing-success-assessment-evaluation-and-reporting-ontario-schools)

---

## 🎨 Design

Branding and visual design created in **Canva** (Design ID: DAHDeUPn5LI).
Edit your design: https://www.canva.com/d/GkVtpvJe3GmqYvM

---

Built with ❤️ for Ontario students.
