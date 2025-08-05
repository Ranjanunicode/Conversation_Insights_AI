# scripts/enrich.py
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Call
from app.services.insight import (
    compute_embedding,
    compute_sentiment_score,
    compute_agent_talk_ratio,
)
import json
from tqdm import tqdm

def enrich():
    db: Session = SessionLocal()
    calls = db.query(Call).all()

    for call in tqdm(calls, desc="Enriching calls"):
        if call.embedding is not None:
            continue  # already enriched

        try:
            call.customer_sentiment_score = compute_sentiment_score(call.transcript)
            call.agent_talk_ratio = compute_agent_talk_ratio(call.transcript)
            call.embedding = json.dumps(compute_embedding(call.transcript))
        except Exception as e:
            print(f"Error enriching call {call.call_id}: {e}")

    db.commit()
    db.close()

if __name__ == "__main__":
    enrich()
