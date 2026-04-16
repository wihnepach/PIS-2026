"""
Юнит-тесты для Session (Aggregate Root)

Проверка инвариантов и доменных событий
"""

import pytest
from domain.models.session import Session
from domain.models.duration import Duration
from domain.models.session_status import SessionStatus
from domain.events.session_events import SessionStarted, SessionCompleted, SessionFailed
from domain.exceptions.domain_exceptions import InvalidSessionStateException


class TestSessionInvariants:
    """Тесты инвариантов Session"""

    def test_should_not_finish_if_not_active(self):
        """Нельзя завершить сессию, если она не ACTIVE"""
        session = Session("s1", "t1", "u1", Duration(25))
        session.fail("error")

        with pytest.raises(InvalidSessionStateException):
            session.finish()

    def test_should_start_with_active_status(self):
        """Сессия должна создаваться в статусе ACTIVE"""
        session = Session("s1", "t1", "u1", Duration(25))
        assert session._status == SessionStatus.ACTIVE

    def test_should_change_status_to_done(self):
        """Сессия должна переходить в DONE"""
        session = Session("s1", "t1", "u1", Duration(25))
        session.finish()

        assert session._status == SessionStatus.DONE


class TestSessionEvents:
    """Тесты доменных событий"""

    def test_should_register_event_when_started(self):
        """Должно регистрироваться событие SessionStarted"""
        session = Session("s1", "t1", "u1", Duration(25))

        events = session._events

        assert len(events) == 1
        assert isinstance(events[0], SessionStarted)
        assert events[0].session_id == "s1"

    def test_should_register_event_when_completed(self):
        """Должно регистрироваться событие SessionCompleted"""
        session = Session("s1", "t1", "u1", Duration(25))
        session.finish()

        events = session._events

        assert any(isinstance(e, SessionCompleted) for e in events)

    def test_should_register_event_when_failed(self):
        """Должно регистрироваться событие SessionFailed"""
        session = Session("s1", "t1", "u1", Duration(25))
        session.fail("error")

        events = session._events

        assert any(isinstance(e, SessionFailed) for e in events)