from operator import attrgetter
import jwDeliveryAPI
from datetime import datetime

class Video:

    def __init__(self, resp):

        self.status = resp['status']
        self.key = resp['key']
        self.title = resp['title']
        self.date = resp['date']
        self.date_as_datetime = datetime.fromtimestamp(int(self.date)).strftime('%m-%d-%Y')
        self.description = resp['description']
        self.duration = resp['duration']
        self.duration_as_time = self.duration.replace('.', ':')
        self.media_type = resp['mediatype']
        self.size = resp['size']
        self.source_format = resp['sourceformat']
        self.source_type = resp['sourcetype']
        self.updated = resp['updated']
        self.md5 = resp['md5']
        self.author = resp['author']
        self.source_URL = resp['sourceurl']
        self.expires_date = resp['expires_date']
        self.link = resp['link']
        self.upload_session_id = resp['upload_session_id']
        self.custom_fields = resp['custom']



        if resp['tags']:
            self.tags = resp['tags'].split(',')
        else:
            self.tags = None

        self.thumbnails = jwDeliveryAPI.thumbnail_list(self.key)




class Video_list:

    def __init__(self, videos):
        self.videos = videos

    def sort(self, property='title', direction='asc'):
        rev = False


        if direction != 'asc':
            rev = True

        sorted_videos = sorted(
                self.videos,
                reverse=rev,
                key=attrgetter(property)
                )

        return sorted_videos


class Conversion:

    def __init__(self, resp):
        self.status = resp['status']
        self.mediatype = resp['mediatype']
        self.height = resp['height']
        self.width = resp['width']
        self.filesize = resp['filesize']
        self.key = resp['key']
        self.duration = resp['duration']
        self.template = Template(resp['template'])
        self.link = "{protocol}://{address}{path}".format(**resp['link'])



class Template:

    def __init__(self, resp):
        self.required = resp['required']
        self.format = {
            'name': resp['format']['name'],
            'key': resp['format']['key']
            }
        self.id = resp['id']
        self.key = resp['key']
        self.name = resp['name']
