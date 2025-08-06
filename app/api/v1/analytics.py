# app/api/analytics.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Call
from sqlalchemy.sql import func
from app.auth.deps import get_current_user

router = APIRouter()

@router.get("/agents", dependencies=[Depends(get_current_user)])
def agent_leaderboard():
    db: Session = SessionLocal()

    rows = db.query(
        Call.agent_id,
        func.count().label("total_calls"),
        func.avg(Call.customer_sentiment_score).label("avg_sentiment"),
        func.avg(Call.agent_talk_ratio).label("avg_talk_ratio")
    ).group_by(Call.agent_id).order_by(func.count().desc()).all()

    return [
        {
            "agent_id": r.agent_id,
            "total_calls": r.total_calls,
            "avg_sentiment": round(r.avg_sentiment or 0, 2),
            "avg_talk_ratio": round(r.avg_talk_ratio or 0, 2)
        }
        for r in rows
    ]
