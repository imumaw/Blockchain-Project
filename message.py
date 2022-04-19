import datetime

class Message:
    """
        Message holds a few pieces of data about a message between 2 users and is similar to an email.

        It contains:
            - The message's sender
            - The message's receiver
            - The time of message
            - The actual message
    """

	def __init__(self, sender, receiver, message):
		self.sender = sender
		self.receiver = receiver
		self.message = message
		self.time = datetime.datetime.now()


	def __repr__(self):
		return f"from: {self.sender}, to: {self.receiver}, at: {self.time.isoformat()}, message: {self.message}"
