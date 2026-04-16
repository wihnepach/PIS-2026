import os
import sys

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

LAB05_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "lab-05")
)
sys.path.insert(0, LAB05_PATH)

from infrastructure.config.database import Base
from infrastructure.adapter.outgoing.request_repository import SessionRepository, SessionOrm


@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_save_request(db_session):
    repo = SessionRepository(db_session)

    session = SessionOrm(
        session_id="s1",
        task_id="t1",
        user_id="u1",
        duration_minutes=25,
        status="ACTIVE",
    )

    repo.save(session)

    result = repo.find_by_id("s1")

    assert result is not None
    assert result.session_id == "s1"


def test_find_by_id(db_session):
    repo = SessionRepository(db_session)

    session = SessionOrm(
        session_id="s2",
        task_id="t2",
        user_id="u2",
        duration_minutes=30,
        status="ACTIVE",
    )

    repo.save(session)

    result = repo.find_by_id("s2")

    assert result is not None
    assert result.task_id == "t2"