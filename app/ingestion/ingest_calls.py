# app/ingestion/ingest_calls.py
import asyncio
from app.db.session import AsyncSessionLocal
from app.models.call import Call
from app.ingestion.transcript_generator import generate_call_json

async def ingest_calls(n=200):
    print(f"Ingesting {n} synthetic calls...")
    async with AsyncSessionLocal() as session:
        calls = []
        for _ in range(n):
            raw_call = await generate_call_json()
            call = Call(
                call_id=raw_call["call_id"],
                agent_id=raw_call["agent_id"],
                customer_id=raw_call["customer_id"],
                language=raw_call["language"],
                start_time=raw_call["start_time"],
                duration_seconds=raw_call["duration_seconds"],
                transcript=raw_call["transcript"],
            )
            calls.append(call)

        session.add_all(calls)
        await session.commit()
        print(f"✅ Done: {n} calls ingested and saved.")

if __name__ == "__main__":
    asyncio.run(ingest_calls(200))


# import asyncio
# import aiohttp
# import uuid
# import random
# import datetime
# from faker import Faker
# from app.db.session import AsyncSessionLocal
# from app.models.call import Call

# fake = Faker()

# async def generate_fake_transcript():
#     return " ".join(fake.sentences(nb=random.randint(10, 50)))

# async def create_fake_call():
#     return Call(
#         call_id=uuid.uuid4(),
#         agent_id=uuid.uuid4(),
#         customer_id=uuid.uuid4(),
#         language="en",
#         start_time=fake.date_time_this_year(),
#         duration_seconds=random.randint(60, 1200),
#         transcript=await generate_fake_transcript()
#     )

# async def ingest_calls(n=200):
#     async with AsyncSessionLocal() as session:
#         calls = [await create_fake_call() for _ in range(n)]
#         session.add_all(calls)
#         await session.commit()

# if __name__ == "__main__":
#     asyncio.run(ingest_calls())