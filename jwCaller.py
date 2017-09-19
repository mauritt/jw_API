from jwController import Controller
from jwCategories import Video, Video_list, Conversion, Track
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

        self.uploader = self.controller.uploader


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

    def get_upload_URL(self,category, update=False, **params):

        if category == 'video':
            controller = self.videos
        elif category == 'thumbnail':
            controller = self.thumbnails
        elif category == 'track':
            controller = self.tracks
        else:
            URL = False

        if update:
            update_response = controller.update(**params)
        else:
            update_response = controller.create(**params)

        print(update_response)
        URL = self.uploader.get_upload_URL(update_response)
        return URL

    def get_conversions(self, key):
        conversions = []
        conversion_list = self.conversions.list(video_key=key)['conversions']
        for conversion in conversion_list:
            conversions.append(Conversion(conversion))
        return conversions

    def get_tracks(self,key):
        tracks=[]
        tracks_list = self.tracks.list(video_key=key)['tracks']
        for track in tracks_list:
            tracks.append(Track(track))
        return tracks

    def create_video(self, file, **params):
        URL = self.get_upload_URL('video', **params)
        self.uploader.upload_file(URL, file)
        return














