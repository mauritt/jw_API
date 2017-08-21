from jwAPI import jwAPI
from jwAPIClasses import API_Classes

class Controller:

	def __init__(self, apiClass, key, secret):
		self.API = jwAPI(key, secret)
		self.apiClass = apiClass
		self.URL = API_Classes[apiClass]['baseURL']

	def __call__(self, action, **params):
		if action in API_Classes[self.apiClass]['actions']:
			URL = self.URL + action
			req = self.API.call(URL, **params)
			return req
