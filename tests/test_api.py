# tests/test_api.py
from tests.factories import create_test_call
from app.db.models import Call
from app.db.session import SessionLocal

def test_list_calls(client):
    response = client.get("/api/v1/calls")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_call_by_id(client):
    db = SessionLocal()
    call = create_test_call()
    db.add(call)
    db.commit()

    response = client.get(f"/api/v1/calls/{call.call_id}")
    assert response.status_code == 200
    assert response.json()["call_id"] == call.call_id

def test_call_recommendations(client):
    db = SessionLocal()
    call1 = create_test_call(agent_id="A1")
    call2 = create_test_call(agent_id="A2")
    db.add_all([call1, call2])
    db.commit()

    response = client.get(f"/api/v1/calls/{call1.call_id}/recommendations")
    assert response.status_code == 200
    assert "recommendations" in response.json()

def test_agent_leaderboard(client):
    db = SessionLocal()
    db.add(create_test_call(agent_id="leader"))
    db.commit()

    response = client.get("/api/v1/analytics/agents")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
