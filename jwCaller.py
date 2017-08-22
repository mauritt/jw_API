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

		self.controller = Controller(self.key, self.secret)

		self.videos = self.controller.API_class('videos')
		self.conversions = self.controller.API_class('conversions')
		self.tags = self.controller.API_class('tags')
		self.tracks = self.controller.API_class('tracks')
		self.thumbnails = self.controller.API_class('thumbnails')




if __name__ == '__main__':

