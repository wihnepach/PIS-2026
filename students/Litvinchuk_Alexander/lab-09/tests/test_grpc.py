import threading
import time

import grpc

import session_service_pb2
import session_service_pb2_grpc

from grpc_app.server import serve


def start_server():
    serve()


def test_grpc_flow():
    thread = threading.Thread(target=start_server, daemon=True)
    thread.start()

    time.sleep(2)

    channel = grpc.insecure_channel("localhost:50051")
    stub = session_service_pb2_grpc.SessionServiceStub(channel)

    # create
    response = stub.CreateSession(
        session_service_pb2.CreateSessionRequest(
            session_id="test1",
            task_id="task",
            user_id="user",
            duration_minutes=20,
        )
    )
    assert response.session_id == "test1"

    # get
    response = stub.GetSession(
        session_service_pb2.GetSessionRequest(session_id="test1")
    )
    assert response.status == "ACTIVE"