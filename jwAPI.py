import time
import random
import hashlib
import os
import requests


class jwAPI:
	"""Performs all communication with the JW Platform API"""

	baseURL = 'https://api.jwplatform.com/v1/'

	def __init__(self, key, secret):
		"""Sets API key and secret for a given JW account"""
		self.api_key = key
		self.api_secret = secret


	def call(self, URL, format = 'json', **params):
		"""Takes URL and parameters returns API response"""
		callURL = self.createURL(URL, format, **params)
		baseURL = callURL['baseURL']
		payload = callURL['payload']
		req = self.makeRequest(baseURL,payload)
		reqResults = req.text
		return reqResults

	@staticmethod
	def makeRequest(URL, payload):
		"""Makes JW Platform API call and returns response."""
		r = requests.get(URL, params = payload)
		return r

	def createURL(self, request, format, **params):
		"""Returns URL formatted for JW API."""
		baseURL = self.baseURL + request
		payload={}
		payload['api_nonce'] = self.getNonce()
		payload['api_timestamp'] = str(int(time.time()))
		payload['api_key'] = self.api_key
		payload['api_format'] = format
		for param in params.keys():
			payload[param] = params[param]

		sbs = ''
		for attr in sorted(payload.keys()):
			sbs += (attr + '=' + payload[attr] + '&')
		sbs = sbs[0:-1]
		auth = sbs+self.api_secret
		auth = auth.encode('utf8')
		sig = hashlib.sha1(auth).hexdigest()
		payload['api_signature'] = hashlib.sha1(auth).hexdigest()

		return {'baseURL': baseURL, 'payload':payload}

	def upload(self, response, vid):
		"""Uploads a file to JW platform"""
		response = json.loads(response)
		protocol = response['link']['protocol']
		address =  response['link']['address']
		path = response['link']['path']
		format = 'xml'
		key = response['link']['query']['key']
		token = response['link']['query']['token']
		URL = "%s://%s%s?api_format=%s&key=%s&token=%s" % (protocol,address,path,format,key,token)
		files = {'file': open(vid, 'rb')}
		r = requests.post(URL, files = files)
		print(r.text)


	@staticmethod
	def getNonce():
		"""Returns random eight-digit number"""
		nonce = ''
		for x in range(0,8):
			rand = str(random.randint(0,9))
			nonce += rand
		return nonce
