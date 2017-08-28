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

    available_players = []



    def __init__(self, key, secret):

        self.key = key
        self.secret = secret


        self.controller = Controller(self.key, self.secret)

        self.videos = self.controller.videos
        self.conversions = self.controller.conversions
        self.tags = self.controller.tags
        self.tracks = self.controller.tracks
        self.thumbnails = self.controller.thumbnails
        self.players = self.controller.players


        for player in self.players.list()['players']:
            available_player = (player['key'])
            self.available_players.append(available_player)


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


    def get_embed(self, video_key, player_key):
        print(self.available_players)

        if player_key not in self.available_players:
            player_key = self.available_players[0]

        embed_URL = "<script src='//content.jwplatform.com/players/{}-{}.js'></script>"

        return embed_URL.format(video_key, player_key)





