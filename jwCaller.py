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
		self.key = accounts[account]['key']
		self.secret = accounts[account]['secret']
		self.API = jwAPI(self.key, self.secret)
		self.videos = Controller('video', self.API)
		self.thumnails = Controller('thumbnail', self.API)
		self.tracks = Controller('track', self.API)
		self.conversions = Controller('conversion', self.API)
		self.views = Controller('view', self.API)
		self.engagements = Controller('engagement', self.API)

if __name__ == '__main__':
	pass