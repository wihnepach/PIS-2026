import os
import sys
import time
from concurrent import futures

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import grpc
import session_service_pb2
import session_service_pb2_grpc


sessions = {}


class SessionService(session_service_pb2_grpc.SessionServiceServicer):
    def CreateSession(self, request, context):
        sessions[request.session_id] = {
            "session_id": request.session_id,
            "task_id": request.task_id,
            "user_id": request.user_id,
            "duration_minutes": request.duration_minutes,
            "status": "ACTIVE",
        }

        return session_service_pb2.SessionResponse(**sessions[request.session_id])

    def GetSession(self, request, context):
        session = sessions.get(request.session_id)

        if not session:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Session not found")
            return session_service_pb2.SessionResponse()

        return session_service_pb2.SessionResponse(**session)

    def StreamActiveSessions(self, request, context):
        while True:
            for session in sessions.values():
                if session["status"] == "ACTIVE":
                    yield session_service_pb2.SessionResponse(**session)
            time.sleep(2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    session_service_pb2_grpc.add_SessionServiceServicer_to_server(
        SessionService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC Server started on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()