# app/ingestion/transcript_generator.py
import uuid
import random
import datetime
import json
from pathlib import Path
from faker import Faker

fake = Faker()
RAW_DIR = Path(__file__).parent / "raw_transcripts"
RAW_DIR.mkdir(exist_ok=True)

async def generate_fake_transcript(n_turns=10):
    conversation = []
    for _ in range(n_turns):
        speaker = random.choice(["Agent", "Customer"])
        text = fake.sentence(nb_words=random.randint(5, 15))
        conversation.append(f"{speaker}: {text}")
    return "\n".join(conversation)

async def generate_call_json():
    call_data = {
        "call_id": str(uuid.uuid4()),
        "agent_id": str(uuid.uuid4()),
        "customer_id": str(uuid.uuid4()),
        "language": "en",
        "start_time": fake.date_time_this_year().isoformat(),
        "duration_seconds": random.randint(60, 1200),
        "transcript": await generate_fake_transcript(random.randint(10, 40))
    }

    # Save raw JSON
    file_path = RAW_DIR / f"{call_data['call_id']}.json"
    with open(file_path, "w") as f:
        json.dump(call_data, f, indent=2)

    return call_data
