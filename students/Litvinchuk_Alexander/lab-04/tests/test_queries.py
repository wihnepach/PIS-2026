import pytest

from application.query.get_session_by_id_query import GetSessionByIdQuery
from application.query.handlers.get_session_by_id_handler import GetSessionByIdHandler
from domain.models.session import Session
from domain.models.duration import Duration


# 🔧 Fake Repository
class FakeSessionRepository:
    def __init__(self):
        self.storage = {}

    def save(self, session):
        self.storage[session.session_id] = session

    def find_by_id(self, session_id):
        return self.storage.get(session_id)


# ✅ ТЕСТ

def test_should_return_session_dto():
    repo = FakeSessionRepository()

    # создаём тестовую сессию
    session = Session("s1", "t1", "u1", Duration(25))
    repo.save(session)

    handler = GetSessionByIdHandler(repo)

    query = GetSessionByIdQuery(session_id="s1")

    result = handler.handle(query)

    assert result.session_id == "s1"
    assert result.task_id == "t1"
    assert result.user_id == "u1"
    assert result.duration_minutes == 25


def test_should_throw_if_not_found():
    repo = FakeSessionRepository()
    handler = GetSessionByIdHandler(repo)

    query = GetSessionByIdQuery(session_id="unknown")

    with pytest.raises(ValueError):
        handler.handle(query)