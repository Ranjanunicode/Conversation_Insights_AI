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
git clone https://github.com/yourusername/call-analytics-service.git
cd call-analytics-service
cp .env.example .env
# Add your GROQ_API_KEY to .env
