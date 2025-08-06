# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import analytics, calls
from app.api.v1.auth import router as auth_router

app = FastAPI(
    title="Call Transcript Analytics API",
    version="1.0.0"
)

# CORS middleware (optional for frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(calls.router, prefix="/api/v1/calls", tags=["Calls"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])

# Optional: WebSocket support
# You can add a new router like: `from app.api.v1 import websocket`
# and then: `app.include_router(websocket.router, prefix="/ws", tags=["WebSocket"])`
