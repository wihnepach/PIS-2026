import pytest

from application.command.create_request_command import CreateRequestCommand
from application.command.handlers.create_request_handler import CreateRequestHandler


# 🔧 Fake Repository (заглушка)
class FakeSessionRepository:
    def __init__(self):
        self.storage = {}

    def save(self, session):
        self.storage[session.session_id] = session

    def find_by_id(self, session_id):
        return self.storage.get(session_id)


# ✅ ТЕСТЫ

def test_should_create_session_successfully():
    repo = FakeSessionRepository()
    handler = CreateRequestHandler(repo)

    command = CreateRequestCommand(
        session_id="s1",
        task_id="t1",
        user_id="u1",
        duration_minutes=25
    )

    result = handler.handle(command)

    # проверка ID
    assert result == "s1"

    # проверка что реально сохранилось
    saved_session = repo.find_by_id("s1")
    assert saved_session is not None
    assert saved_session.task_id == "t1"
    assert saved_session.user_id == "u1"


def test_should_fail_if_duration_invalid():
    with pytest.raises(ValueError):
        CreateRequestCommand(
            session_id="s1",
            task_id="t1",
            user_id="u1",
            duration_minutes=0
        )


def test_should_store_session_in_repository():
    repo = FakeSessionRepository()
    handler = CreateRequestHandler(repo)

    command = CreateRequestCommand(
        session_id="s2",
        task_id="t2",
        user_id="u2",
        duration_minutes=30
    )

    handler.handle(command)

    assert "s2" in repo.storage