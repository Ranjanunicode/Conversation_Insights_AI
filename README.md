# Conversation_Insights_AI

# 📞 Call Transcript Analytics Microservice

This is a production-ready Python microservice that ingests synthetic sales call transcripts, stores them in a SQLite database, enriches them using AI (via Groq and Hugging Face), and serves insights via a REST API built with FastAPI.

---

## 📌 Features

- 🔄 Async ingestion of 200+ synthetic transcripts using Faker + Groq
- 🧠 AI enrichment: sentiment scoring, agent talk ratio, embeddings
- 🔍 Queryable & filterable API for calls and analytics
- 🧭 Recommendations + coaching nudges via LLM
- ✅ SQLite + SQLAlchemy + Pydantic models
- 🧪 Test coverage ≥90% (pytest + coverage)
- 🐳 Docker + GitHub Actions CI ready

---

## ⚙️ Setup Instructions

### 🔐 1. Clone and Configure
```bash
git clone https://github.com/Ranjanunicode/Conversation_Insights_AI.git
cd Conversation_Insights_AI
touch .env
nano .env
# Add your GROQ_API_KEY to .env
```

---

# 🔎 Example Usage

## ✅ Get All Calls
```bash
curl -H "Authorization: Bearer <your_jwt_token>" http://localhost:8000/api/v1/calls
```

## ✅ Get One Call
```bash
curl -H "Authorization: Bearer <your_jwt_token>" http://localhost:8000/api/v1/calls/<call_id>
```

## ✅ Get Recommendations for a Call
```bash
curl -H "Authorization: Bearer <your_jwt_token>" http://localhost:8000/api/v1/calls/<call_id>/recommendations
```

## ✅ Get Agent Leaderboard
```bash
curl -H "Authorization: Bearer <your_jwt_token>" http://localhost:8000/api/v1/analytics/agents

