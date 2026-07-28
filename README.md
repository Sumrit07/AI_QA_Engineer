# 🤖 AI QA Engineer

An AI-powered Software Quality Assurance Platform that automatically analyzes software projects, detects bugs, identifies security vulnerabilities, evaluates code quality, generates PDF reports, and provides AI-powered code fixes using **Google Gemini AI**, **Ollama**, **FastAPI**, and **LangGraph**.

---

## 🚀 Features

- 📂 Upload complete project as a ZIP file
- 🤖 AI-powered code analysis
- 🐞 Automatic Bug Detection
- 🔒 Security Vulnerability Analysis
- ⚡ Performance Optimization Suggestions
- 🧹 Code Smell Detection
- 🧠 Root Cause Analysis
- 🛠 Auto Fix Entire Project
- 📄 Professional PDF Report Generation
- 📊 Quality Score & Coverage Dashboard
- 📈 Interactive Charts
- 🧪 AI Test Case Generation
- ✅ Test Coverage Analysis
- 🔑 JWT Authentication System
- 📜 Analysis History

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
          FastAPI Backend
                  │
     ┌────────────┼────────────┐
     │            │            │
     ▼            ▼            ▼
 AI Agents     Database     Frontend
     │            │            │
     ▼            ▼            ▼
 Gemini AI     PostgreSQL   Dashboard
     │
     ▼
  PDF Report
```

---

# 🤖 AI Agents

The platform uses multiple AI agents to perform software quality analysis.

| Agent | Purpose |
|--------|----------|
| 🐞 Bug Detector | Detect runtime, syntax and logical bugs |
| 🔒 Security Agent | Detect security vulnerabilities |
| ⚡ Performance Agent | Find performance bottlenecks |
| 🧹 Code Smell Agent | Detect maintainability issues |
| 🧠 Root Cause Agent | Explain why bugs occur |
| 📄 Report Generator | Generate executive summary |
| ⭐ Project Score Agent | Calculate project quality score |
| 🧪 Test Generator | Generate unit tests |
| ✅ Coverage Agent | Analyze test coverage |

---

# 📊 Dashboard

The dashboard provides

- Project Quality Score
- Security Score
- Test Coverage
- Recent Analysis
- Analysis History
- AI Report
- Charts
- Auto Fix Project

---

# 🛠 Tech Stack

## Backend

- FastAPI
- Python
- SQLAlchemy
- JWT Authentication

## AI

- Google Gemini AI
- Ollama
- LangChain
- LangGraph

## Database

- PostgreSQL

## Frontend

- HTML
- CSS
- JavaScript
- Chart.js

## Reports

- ReportLab PDF

---

# 📂 Project Structure

```
AI_QA_Engineer/

│
├── backend/
│   ├── agents/
│   ├── api/
│   ├── config/
│   ├── database/
│   ├── dependencies/
│   ├── models/
│   ├── prompts/
│   ├── services/
│   └── utils/
│
├── frontend/
│   ├── css/
│   ├── js/
│   └── dashboard.html
│
├── tests/
│
├── requirements.txt
├── README.md
└── main.py
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Sumrit07/AI_QA_Engineer.git

cd AI_QA_Engineer
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
DATABASE_URL=your_database_url

GEMINI_API_KEY=your_api_key

SECRET_KEY=your_secret_key
```

---

# ▶️ Run Project

```bash
uvicorn backend.main:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

# 📄 Reports

The platform generates

- Executive Summary
- Bug Report
- Security Report
- Performance Report
- Code Smells
- Recommendations
- PDF Report

---

# 🎯 Future Improvements

- Multi-language Code Analysis
- Docker Support
- Kubernetes Deployment
- CI/CD Integration
- GitHub Repository Scanning
- SonarQube Integration
- Slack Notifications
- Email Reports

---

# 👨‍💻 Author

**Sumrit Singh**

B.Tech Computer Science Engineering

GitHub

https://github.com/Sumrit07

---

# ⭐ Support

If you like this project, don't forget to ⭐ the repository.

---

# 📜 License

This project is developed for educational and portfolio purposes.