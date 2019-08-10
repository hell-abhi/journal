class user:
    username = ""
    password = ""

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def __str__(self):
        return "username: " + self.username + " password: " + self.password

    def __eq__(self, other):
        if isinstance(other, user):
            return self.username == other.password and self.password == other.password 
        return False
