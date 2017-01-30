"""
Movie Class

Creates a movie object with a youtube trailer, poster art and title

"""


class Movie(object):
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Movie constructor

        Parameters
        ----------
        title : string
            title of the movie

        poster_image_url : string
            image of the poster art for the movie

        trailer_youtube_url : string
            youtube url
        """
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.title = title
