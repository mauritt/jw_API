from jwAccounts import accounts
from jwAPI import jwAPI
from jwController import Controller
import json
import os
import requests
from pprint import PrettyPrinter
import time



class jwCaller:

	def __init__(self,account, key, secret):
		self.account = account
		self.key = key
		self.secret = secret
		self.API = jwAPI(self.key, self.secret)
		self.videos = Controller('video', self.API)
		self.thumbnails = Controller('thumbnail', self.API)
		self.tracks = Controller('track', self.API)
		self.conversions = Controller('conversion', self.API)
		# self.views = Controller('view', self.API) Moved to accounts/usage
		# self.engagements = Controller('engagement', self.API) Moved to accounts/usage

if __name__ == '__main__':
	account = accounts['corpu-customers']
	test = jwCaller(account)
	print(test.status)
