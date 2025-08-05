from sqlalchemy import Column, String, DateTime, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid
import datetime

Base = declarative_base()

class Call(Base):
    __tablename__ = "calls"

    call_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agent_id = Column(UUID(as_uuid=True), nullable=False)
    customer_id = Column(UUID(as_uuid=True), nullable=False)
    language = Column(String(10), default="en")
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    duration_seconds = Column(Integer, nullable=False)
    transcript = Column(Text, nullable=False)