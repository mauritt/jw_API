from jwAccounts import accounts
from jwAPI import jwAPI
from jwController import Controller
import json
import os
import requests
from pprint import PrettyPrinter
import time



class jwCaller:

	def __init__(self,account):
		self.account = account
		self.key = account['key']
		self.secret = account['secret']
		self.API = jwAPI(self.key, self.secret)
		self.videos = Controller('video', self.API)
		self.thumbnails = Controller('thumbnail', self.API)
		self.tracks = Controller('track', self.API)
		self.conversions = Controller('conversion', self.API)
		# self.views = Controller('view', self.API) Moved to accounts/usage
		# self.engagements = Controller('engagement', self.API) Moved to accounts/usage

if __name__ == '__main__':
	pass
