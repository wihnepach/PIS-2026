class Duration:
    def __init__(self, minutes: int):
        if minutes <= 0:
            raise ValueError("Длительность должна быть больше 0")
        self.minutes = minutes

    def __eq__(self, other):
        return isinstance(other, Duration) and self.minutes == other.minutes

    def __repr__(self):
        return f"Duration({self.minutes} min)"