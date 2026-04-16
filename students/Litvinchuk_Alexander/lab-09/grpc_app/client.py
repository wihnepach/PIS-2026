import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import grpc
import session_service_pb2
import session_service_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = session_service_pb2_grpc.SessionServiceStub(channel)

    # 1. Создание сессии
    create_response = stub.CreateSession(
        session_service_pb2.CreateSessionRequest(
            session_id="s1",
            task_id="t1",
            user_id="u1",
            duration_minutes=25,
        )
    )
    print("Created session:")
    print(create_response)

    # 2. Получение сессии
    get_response = stub.GetSession(
        session_service_pb2.GetSessionRequest(session_id="s1")
    )
    print("Fetched session:")
    print(get_response)

    # 3. Поток активных сессий
    print("Streaming active sessions:")
    stream = stub.StreamActiveSessions(session_service_pb2.Empty())
    for i, session in enumerate(stream):
        print(session)
        if i >= 2:
            break


if __name__ == "__main__":
    run()