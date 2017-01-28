class Movie(object):
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.title = title
