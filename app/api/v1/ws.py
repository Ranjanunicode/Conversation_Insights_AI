from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from transformers import pipeline

router = APIRouter()

# Load sentiment model once
sentiment_analyzer = pipeline("sentiment-analysis")

@router.websocket("/ws/sentiment")
async def websocket_sentiment(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            result = sentiment_analyzer(data)[0]  # e.g., {'label': 'POSITIVE', 'score': 0.999}
            await websocket.send_json({
                "input": data,
                "label": result["label"],
                "score": round(result["score"], 3)
            })
    except WebSocketDisconnect:
        print("Client disconnected")
