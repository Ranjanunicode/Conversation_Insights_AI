# app/schemas/calls.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CallOut(BaseModel):
    call_id: str
    agent_id: str
    customer_id: str
    language: str
    start_time: datetime
    duration_seconds: int
    transcript: str
    agent_talk_ratio: Optional[float]
    customer_sentiment_score: Optional[float]

    class Config:
        orm_mode = True
