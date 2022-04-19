import datetime

class Transaction:

	#initilizer creates the data about the transaction that happened
	def __init__(self, sender, receiver, data):
		self.sender = sender
		self.receiver = receiver
		self.data = data
		self.time = datetime.datetime.now()


	def to_dictionary(self):
	#method to create dictionary for easy viewing information

		#turn data into dictionary
		return {
			"sender" : self.sender,
			"reciver" : self.receiver,
			"data" : self.data,
			"time" : self.time.isoformat()
		}
