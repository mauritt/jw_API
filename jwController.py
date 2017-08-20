class Controller:
	URLs = {
			'video': 'videos/',
			'tag': 'videos/tags/',
			# 'view':'videos/views/', Moved to accounts/usage
			'track':'videos/tracks/',
			'thumbnail':'videos/thumbnails/',
			# 'engagement':'videos/engagements/', Moved to accounts/usage
			'conversion':'videos/conversions/',
			'account': 'accounts/',
			'tags': 'accounts/tags/',
			'usage': 'accounts/usage/',
			'channels': 'channels/',
			'channels-videos': 'channels/videos',
			'players': 'players/',
			'status': 'status/',
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





