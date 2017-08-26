from jwAPI import jwAPI
from jwAPIClasses import API_Classes
import json

class API_class:

    def __init__(self, baseURL, allowed_actions, API):

        self.allowed_actions = allowed_actions
        self.baseURL = baseURL
        self.API = API


        if "list" in allowed_actions:
            self.list = API_action(baseURL, 'list', API)

        if "show" in allowed_actions:
            self.show = API_action(baseURL, 'show', API)

        if "create" in allowed_actions:
            self.create = API_action(baseURL, 'create', API)

        if "delete" in allowed_actions:
            self.delete = API_action(baseURL, 'delete', API)

        if "update" in allowed_actions:
            self.update = API_action(baseURL, 'update', API)



class API_action:

    def __init__(self, baseURL, action, API):
        self.API = API
        self.action = action
        self.baseURL = baseURL

    def __call__(self, file=False, **params):


        URL = "{}{}".format(self.baseURL, self.action)

        req = self.API.call(URL, **params)

        res =  json.loads(req)

        if file and 'file_name' in params.keys():
            res = self.API.upload(res, file)

        return res


class Controller:

    def __init__(self, key, secret):
        self.API = jwAPI(key, secret)

        self.videos = API_class('videos/',API_Classes['videos']['actions'], self.API)
        self.thumbnails = API_class('videos/thumbnails',API_Classes['thumbnails']['actions'], self.API)
        self.tags = API_class('videos/tags',API_Classes['tags']['actions'], self.API)
        self.conversions = API_class('videos/conversions',API_Classes['conversions']['actions'], self.API)
        self.tracks = API_class('videos/tracks',API_Classes['tracks']['actions'], self.API)
        self.players = API_class('players/',API_Classes['players']['actions'], self.API)
