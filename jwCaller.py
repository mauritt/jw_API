from jwAccounts import accounts
from jwAPI import jwAPI
from jwController import Controller
import json
import os
import requests
from pprint import PrettyPrinter
import time



class Account:

    delivery_URL = "https://cdn.jwplayer.com"

    def __init__(self, key, secret):

        self.key = key
        self.secret = secret


        self.controller = Controller(self.key, self.secret)

        self.videos = self.controller.API_class('videos')
        self.conversions = self.controller.API_class('conversions')
        self.tags = self.controller.API_class('tags')
        self.tracks = self.controller.API_class('tracks')
        self.thumbnails = self.controller.API_class('thumbnails')

    def get_thumbnail(self, video_key, thumb_width='720'):
        allowed_widths = [
            '40',
            '120',
            '320',
            '480',
            '640',
            '720',
            '1280'
            '1920'
            ]

        if thumb_width not in allowed_widths:
            thumb_width = '720'

        thumb_URL = "{}/thumbs/{}-{}.jpg"
        return thumb_URL.format(self.delivery_URL, video_key, thumb_width)


