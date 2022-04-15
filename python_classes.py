# libraries
import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5



class Client:
	
	def __init__(self):

		#initialize a random number to seed the key generating function
		random  = Crypto.Random.new().read 

		#encryption function (this one from the RSA library) creates a hash that is 1024 bits long and is seeded by the random input
		#in the proggram this is needed to identify yourself
		self._private_key = RSA.generate(1024, random)

		#not entirely sure on this step but think that the publckey method rehashes it into another identifying code
		#used by public to identify your transactions	
		self._public_key = self._private_key.publickey()
		
		#this method is used to view the public key in a readable way
		#returns a hex string of the key
		def identity(self):
				return binascii.hexlify(self._public_key.exportKey(format='DER'))
.decode('ascii') #returns the hex representation of the public key



class Transaction:

	#initilizer creates the data about the transaction that happened
	def __init__(self, sender, reciver, transaction):
		self.sender = sender
		self.revicer = reciver
		self.transaction = transaction
		self.time = datetime.datetime.now()

	def to_dictionary(self):
	#method to create dictionary for easy viewing information

		#if statement to keep initial creator secret
		if (self.sender = "inital creator"):
			identity = "initial creator"
		else:
			identity = self.sender.identity

		#turn data into dictionary
		return collections.Orderdict({
		"sender" : identity,
		"reciver" : self.reciver,
		"transaction" : self.transaction,
		"time" : self.time
		})

	def sign_transaction(self):
		#purpose of this part is to show and verify who send it
		
		#acessing the private key from the sender (it is a private member)
		private_key = self.sender._private_key
		
		#hashing th ething into a new encrypted thing
		signer = PKCS1_v1_5.new(private_key)
		#no clue what this thing is doing
		h = SHA.new(str(self.to_dict()).encode('utf8'))
		#returning the hex representation of the signature were putting on the transaction
		return binascii.hexlify(signer.sign(h)).decode('ascii')


		

			




