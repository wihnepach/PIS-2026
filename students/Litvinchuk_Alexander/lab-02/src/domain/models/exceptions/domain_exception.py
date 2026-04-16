class DomainException(Exception):
    pass


class InvalidSessionStateException(DomainException):
    pass


class TaskAlreadyCompletedException(DomainException):
    pass


class ActiveSessionExistsException(DomainException):
    pass