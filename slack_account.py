class SlackAccount:
    def __init__(self, token, channel, icon_url, user_name):
        self.token = token
        self.channel = channel
        self.icon_url = icon_url
        self.user_name = user_name

    def post_message(self):
        