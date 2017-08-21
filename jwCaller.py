from jwAccounts import accounts
from jwAPI import jwAPI
from jwController import Controller
import json
import os
import requests
from pprint import PrettyPrinter
import time



class Account:

	def __init__(self, key, secret):
		self.key = key
		self.secret = secret
		self.videos = Controller('videos', key, secret)


if __name__ == '__main__':
	account = accounts['corpu-customers']
	test = Account(account['key'], account['secret'])
	print(test.videos('list'))
