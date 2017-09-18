from jwAPI import jwAPI
from jwAPIClasses import API_Classes
import json
from time import time, sleep


class Controller:

    remaining_calls = 60
    reset = time()


    def __init__(self, key, secret):
        self.API = jwAPI(key, secret)

        self.videos = self.API_class('videos/',API_Classes['videos']['actions'], self)
        self.thumbnails = self.API_class('videos/thumbnails/',API_Classes['thumbnails']['actions'], self)
        self.tags = self.API_class('videos/tags/',API_Classes['tags']['actions'], self)
        self.conversions = self.API_class('videos/conversions/',API_Classes['conversions']['actions'], self)
        self.tracks = self.API_class('videos/tracks/',API_Classes['tracks']['actions'], self)
        self.players = self.API_class('players/',API_Classes['players']['actions'], self)

        self.uploader = self.Uploader(self)



    class API_class:

        def __init__(self, baseURL, allowed_actions, controller):

            self.allowed_actions = allowed_actions
            self.baseURL = baseURL
            self.API = controller.API
            self.action = controller.API_action
            self.errorHandler = controller.errorHandler


            if "list" in allowed_actions:
                self.list = self.errorHandler(self.action(baseURL, 'list', self.API), controller)

            if "show" in allowed_actions:
                self.show = self.action(baseURL, 'show', self.API)
            if "create" in allowed_actions:
                self.create = self.action(baseURL, 'create', self.API)

            if "delete" in allowed_actions:
                self.delete = self.action(baseURL, 'delete', self.API)

            if "update" in allowed_actions:
                self.update = self.action(baseURL, 'update', self.API)


    class API_action:

        def __init__(self, baseURL, action, API):
            self.API = API
            self.action = action
            self.baseURL = baseURL

        def __call__(self, **params):


            URL = "{}{}".format(self.baseURL, self.action)

            req = self.API.call(URL, **params)

            res =  json.loads(req)

            return res


    class Uploader:

        def __init__(self, controller):

            self.controller = controller
            self.API = controller.API

        def get_upload_URL(self, res):
            return self.API.create_upload_URL(res)

        def upload_file(self, URL, file):
            self.API.upload(URL, file)


    class errorHandler:

        def __init__(self, API_Class, controller):
            self.API_Class = API_Class
            self.controller = controller

        def __call__(self, *argv, **kwargs):
            self.rate_limiter()
            resp = self.API_Class(*argv,**kwargs)
            self.rate_recorder(resp)
            return resp

        def rate_limiter(self):
            if self.controller.remaining_calls == 0 and self.controller.reset > int(time()):
                sleep_time = self.controller.reset - int(time())
                sleep(sleep_time)

        def rate_recorder(self, resp):
            if 'rate_limit' in resp.keys():
                self.controller.remaining_calls = resp['rate_limit']['remaining']
                self.controller.reset = resp['rate_limit']['reset']

            return


















