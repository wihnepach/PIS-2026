from enum import Enum


class SessionStatus(Enum):
    ACTIVE = "ACTIVE"
    DONE = "DONE"
    FAILED = "FAILED"