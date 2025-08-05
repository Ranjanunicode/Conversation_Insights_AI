# scripts/ingest.py
import asyncio
import os
import json
import uuid
import random
from faker import Faker
from tqdm import tqdm
from sqlalchemy.orm import Session

from app.db.models import Base, Call
from app.db.session import engine, SessionLocal
from app.utils.groq_client import generate_transcript

fake = Faker()

async def generate_call():
    call_id = str(uuid.uuid4())
    agent_id = str(uuid.uuid4())
    customer_id = str(uuid.uuid4())
    language = "en"
    start_time = fake.date_time_this_year()
    duration_seconds = random.randint(60, 600)

    transcript = await generate_transcript()

    # Save raw JSON
    os.makedirs("data/raw", exist_ok=True)
    with open(f"data/raw/{call_id}.json", "w") as f:
        json.dump({
            "call_id": call_id,
            "agent_id": agent_id,
            "customer_id": customer_id,
            "language": language,
            "start_time": str(start_time),
            "duration_seconds": duration_seconds,
            "transcript": transcript
        }, f, indent=2)

    return Call(
        call_id=call_id,
        agent_id=agent_id,
        customer_id=customer_id,
        language=language,
        start_time=start_time,
        duration_seconds=duration_seconds,
        transcript=transcript
    )

async def ingest(n=200):
    async def batch():
        tasks = [generate_call() for _ in range(n)]
        return await asyncio.gather(*tasks)

    calls = await batch()

    db: Session = SessionLocal()
    db.add_all(calls)
    db.commit()
    db.close()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()  # Fix for "asyncio.run in running loop"

    Base.metadata.create_all(bind=engine)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(ingest())