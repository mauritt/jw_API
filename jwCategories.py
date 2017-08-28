

class Video:

    def __init__(self, resp):

        self.status = resp['status']
        self.key = resp['key']
        self.title = resp['title']
        self.date = resp['date']
        self.description = resp['description']
        self.duration = resp['duration']
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
