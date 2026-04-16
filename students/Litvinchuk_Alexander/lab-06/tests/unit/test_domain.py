import os
import sys

import pytest

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "lab-03", "examples")
    )
)

from domain.models.session import Session
from domain.models.duration import Duration
from domain.models.session_status import SessionStatus
from domain.events.session_events import SessionStarted, SessionCompleted, SessionFailed
from domain.exceptions.domain_exceptions import InvalidSessionStateException


class TestSessionInvariants:
    def test_should_not_finish_if_not_active(self):
        session = Session("s1", "t1", "u1", Duration(25))
        session.fail("error")

        with pytest.raises(InvalidSessionStateException):
            session.finish()

    def test_should_start_with_active_status(self):
        session = Session("s1", "t1", "u1", Duration(25))
        assert session._status == SessionStatus.ACTIVE

    def test_should_change_status_to_done(self):
        session = Session("s1", "t1", "u1", Duration(25))
        session.finish()
        assert session._status == SessionStatus.DONE


class TestSessionEvents:
    def test_should_register_event_when_started(self):
        session = Session("s1", "t1", "u1", Duration(25))
        events = session._events

        assert len(events) == 1
        assert isinstance(events[0], SessionStarted)
        assert events[0].session_id == "s1"

    def test_should_register_event_when_completed(self):
        session = Session("s1", "t1", "u1", Duration(25))
        session.finish()
        events = session._events

        assert any(isinstance(e, SessionCompleted) for e in events)

    def test_should_register_event_when_failed(self):
        session = Session("s1", "t1", "u1", Duration(25))
        session.fail("error")
        events = session._events

        assert any(isinstance(e, SessionFailed) for e in events)


class TestDurationValueObject:
    def test_should_create_valid_duration(self):
        duration = Duration(25)
        assert duration.minutes == 25

    def test_should_not_allow_zero_or_negative_duration(self):
        with pytest.raises(Exception):
            Duration(0)