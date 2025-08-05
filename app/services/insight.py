# app/services/insight.py
import json
import re
from typing import List
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load sentiment pipeline and embedding model once
sentiment_analyzer = pipeline("sentiment-analysis")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_sentiment_score(text: str) -> float:
    """Return sentiment score from -1 to +1"""
    results = sentiment_analyzer(text[:512])  # truncate for speed
    label = results[0]["label"]
    score = results[0]["score"]
    return score if label == "POSITIVE" else -score

def compute_embedding(text: str) -> List[float]:
    return embedding_model.encode(text).tolist()

def compute_agent_talk_ratio(transcript: str) -> float:
    agent_words, customer_words = 0, 0
    for line in transcript.split("\n"):
        line = line.strip()
        if line.lower().startswith("agent:"):
            agent_words += len(re.findall(r'\w+', line[len("agent:"):]))
        elif line.lower().startswith("customer:"):
            customer_words += len(re.findall(r'\w+', line[len("customer:"):]))
    total_words = agent_words + customer_words
    print(agent_words)
    print(customer_words)
    print(total_words)
    return round(agent_words / total_words, 3) if total_words else 0.0


def cosine_sim(emb1: List[float], emb2: List[float]) -> float:
    return cosine_similarity([emb1], [emb2])[0][0]
