class Player:
    def __init__(self, username: str, is_x: bool, is_bot: bool):
        self.username = username
        self.is_x = is_x
        self.is_bot = is_bot

    def get_username(self):
        return self.username

    def user_is_x(self):
        return self.is_x

    def user_is_bot(self):
        return self.is_bot
