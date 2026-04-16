from fastapi import FastAPI
from event_bus.rabbitmq_config import EventBus

app = FastAPI()
bus = EventBus()


sessions = {}


@app.post("/sessions")
def create_session(session_id: str):
    sessions[session_id] = "ACTIVE"

    bus.publish("SessionStarted", {"session_id": session_id})

    return {"session_id": session_id}


@app.post("/sessions/{session_id}/finish")
def finish_session(session_id: str):
    sessions[session_id] = "DONE"

    bus.publish("SessionCompleted", {"session_id": session_id})

    return {"status": "DONE"}