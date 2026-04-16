from domain.exceptions.domain_exceptions import InvalidSessionStateException


class Duration:
    def __init__(self, minutes: int):
        if minutes <= 0:
            raise InvalidSessionStateException("Длительность должна быть > 0")
        self.minutes = minutes