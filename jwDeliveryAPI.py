baseURL = "https://cdn.jwplayer.com"

poster_widths = [
            '40',
            '120',
            '320',
            '480',
            '640',
            '720',
            '1280'
            '1920'
            ]

def dowload_URL(media_id, template_id, media_extension):
    URL_template = "{}/videos/{}-{}.{}"
    download_URL = URL_template.format(baseURL, media_id, template_id, media_extension)
    return download_URL


def thumbnail_URL(video_key, thumb_width='720'):

    if thumb_width not in poster_widths:
        thumb_width = '720'


    URL_template = "{}/thumbs/{}-{}.jpg"
    thumbnail_URL = URL_template.format(baseURL, video_key, thumb_width)
    return thumbnail_URL


def thumbnail_list(video_key):
    thumbnails = {}
    for width in poster_widths:
        thumbnail = thumbnail_URL(video_key, width)
        thumbnails[width] = thumbnail

    return thumbnails

def get_embed(video_key, player_key):

        if player_key not in self.available_players:
            player_key = self.available_players[0]

        embed_URL = "<script src='//content.jwplatform.com/players/{}-{}.js'></script>"

        return embed_URL.format(video_key, player_key)

