# app/api/calls.py
from fastapi import APIRouter, Query, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Call
from app.schemas.calls import CallOut
from typing import List, Optional
import json
from app.services.insight import cosine_sim

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[CallOut])
def list_calls(
    limit: int = Query(10, le=100),
    offset: int = 0,
    agent_id: Optional[str] = None,
    from_date: Optional[str] = None,
    to_date: Optional[str] = None,
    min_sentiment: Optional[float] = None,
    max_sentiment: Optional[float] = None
):
    db = next(get_db())
    query = db.query(Call)

    if agent_id:
        query = query.filter(Call.agent_id == agent_id)
    if from_date:
        query = query.filter(Call.start_time >= from_date)
    if to_date:
        query = query.filter(Call.start_time <= to_date)
    if min_sentiment:
        query = query.filter(Call.customer_sentiment_score >= min_sentiment)
    if max_sentiment:
        query = query.filter(Call.customer_sentiment_score <= max_sentiment)

    return query.offset(offset).limit(limit).all()

@router.get("/{call_id}", response_model=CallOut)
def get_call(call_id: str):
    db = next(get_db())
    call = db.query(Call).filter(Call.call_id == call_id).first()
    if not call:
        raise HTTPException(status_code=404, detail="Call not found")
    return call

@router.get("/{call_id}/recommendations")
def get_similar_calls(call_id: str):
    db = next(get_db())
    base_call = db.query(Call).filter(Call.call_id == call_id).first()
    if not base_call:
        raise HTTPException(status_code=404, detail="Call not found")
    if not base_call.embedding:
        raise HTTPException(status_code=400, detail="Call not enriched")

    base_emb = json.loads(base_call.embedding)

    all_calls = db.query(Call).filter(Call.call_id != call_id).all()
    similarities = []

    for other in all_calls:
        if other.embedding:
            score = cosine_sim(base_emb, json.loads(other.embedding))
            similarities.append((score, other))

    top_5 = sorted(similarities, key=lambda x: x[0], reverse=True)[:5]

    recommendations = [
        {
            "call_id": call.call_id,
            "similarity": round(sim, 3),
            "agent_id": call.agent_id,
            "start_time": call.start_time,
            "sentiment": call.customer_sentiment_score
        }
        for sim, call in top_5
    ]

    nudges = [
        "Try letting the customer talk more.",
        "Use positive reinforcement when customer hesitates.",
        "Summarize benefits clearly after listing features."
    ]

    return {"recommendations": recommendations, "nudges": nudges[:3]}
