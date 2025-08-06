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