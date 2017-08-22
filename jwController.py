from jwAPI import jwAPI
from jwAPIClasses import API_Classes

class Controller:

	def __init__(self, key, secret):
		self.API = jwAPI(key, secret)


	def API_class(self, API_Class):

		def action(action, **params):
			if action in API_Classes[API_Class]['actions']:
				URL = API_Classes[API_Class]['baseURL'] + action
				req = self.API.call(URL, **params)
				return req

		return action
