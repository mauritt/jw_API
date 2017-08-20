class Controller:
	URLs = {
			'video': 'videos/',
			'tag': 'videos/tags/',
			'view':'videos/views/',
			'track':'videos/tracks/',
			'thumbnail':'videos/thumbnails/',
			'engagement':'videos/engagements/',
			'conversion':'videos/conversions/'
		}


	def __init__(self, apiClass, API):
		self.API = API
		self.URL = self.URLs[apiClass]

	def showAll(self, **params):
		"""Returns info for multiple items of a particular JW Platform class"""
		URL = self.URL + 'list'
		req = self.API.call(URL, **params)
		return req


	def show(self, **params):
		"""Returns info for a single item of a particular JW Platform class"""
		URL = self.URL + 'show'
		req = self.API.call(URL, **params)
		return req

	def create(self, **params):
		"""Creates a new instance of a particular JW Platform class"""
		URL = self.URL + 'create'
		req = self.API.call(URL, **params)
		return req

	def delete(self, **params):
		"""Deletes an instance of a particular JW Platform class"""
		URL = self.URL + 'delete'
		req = self.API.call(URL, **params)
		return req

	def update(self, **params):
		URL = self.URL + 'update'
		req = self.API.call(URL, **params)
		return req




