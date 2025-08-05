# tests/factories.py
from app.db.models import Call
import uuid
import datetime

def create_test_call(agent_id: str = "test-agent"):
    return Call(
        call_id=str(uuid.uuid4()),
        agent_id=agent_id,
        customer_id=str(uuid.uuid4()),
        language="en",
        start_time=datetime.datetime.utcnow(),
        duration_seconds=300,
        transcript="Agent: Hello\nCustomer: Hi, I’m interested in a new phone.",
        agent_talk_ratio=0.5,
        customer_sentiment_score=0.75,
        embedding="[0.1, 0.2, 0.3]"  # Dummy embedding
    )
