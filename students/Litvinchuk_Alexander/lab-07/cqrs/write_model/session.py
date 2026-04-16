class Session:
    def __init__(self, session_id: str, status: str = "ACTIVE"):
        self.session_id = session_id
        self.status = status
        self.events = []

    def start(self):
        self.events.append(("SessionStarted", self.session_id))

    def finish(self):
        self.status = "DONE"
        self.events.append(("SessionCompleted", self.session_id))

    def fail(self):
        self.status = "FAILED"
        self.events.append(("SessionFailed", self.session_id))