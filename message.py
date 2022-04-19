import datetime

class Message:

	#initilizer creates the data about the message
	def __init__(self, sender, receiver, message):
		self.sender = sender
		self.receiver = receiver
		self.message = message
		self.time = datetime.datetime.now()


	def __repr__(self):
		return f"from: {self.sender}, to: {self.receiver}, at: {self.time.isoformat()}, message: {self.message}"
