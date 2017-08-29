from jwController import Controller
from jwCategories import Video, Video_list
import os




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


    def get_video(self, key, **params):
        video = self.videos.show(video_key=key, **params)['video']
        return Video(video)

    def get_video_list(self, **params):
        video_list = []
        for video in self.videos.list(**params)['videos']:
            video_list.append(Video(video))
        return Video_list(video_list)
