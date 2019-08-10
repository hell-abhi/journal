class journal:
    timestamp = ""
    entry = ""
    username = ""

    def __init__(self, timestamp, entry, username):

        self.timestamp = timestamp
        self.entry = entry
        self.username = username

    def __str__(self):
        return "timestamp: " + self.timestamp + " entry: " + self.entry + " username: " + self.username

    def __eq__(self, other):
        if isinstance(other, user):
            return self.timestamp == other.timestamp and self.entry == other.entry and self.username == other.username
        return False
