import datetime
class Message:
    def __init__(self, text, sender, recipient):
        self.text = text
        self.sender = sender
        self.recipient = recipient
        self.time = datetime.now()
        self.readCount = 0


