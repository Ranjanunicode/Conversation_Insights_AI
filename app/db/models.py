# app/db/models.py
from sqlalchemy import Column, String, Integer, DateTime, Text, Float
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Call(Base):
    __tablename__ = "calls"

    call_id = Column(String, primary_key=True)
    agent_id = Column(String, index=True)
    customer_id = Column(String)
    language = Column(String)
    start_time = Column(DateTime, default=datetime.datetime.utcnow, index=True)
    duration_seconds = Column(Integer)
    transcript = Column(Text)

    agent_talk_ratio = Column(Float, nullable=True)
    customer_sentiment_score = Column(Float, nullable=True)
    embedding = Column(Text, nullable=True)  # JSON-encoded list
