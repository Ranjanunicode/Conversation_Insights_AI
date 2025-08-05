# app/main.py
from fastapi import FastAPI
from app.api.v1 import analytics
from app.api.v1 import calls

app = FastAPI(
    title="Call Transcript Analytics API",
    version="1.0.0"
)

app.include_router(calls.router, prefix="/api/v1/calls", tags=["Calls"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])