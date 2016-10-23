class Movie():
    """ This class provides a way to store movie related information

    Attributes:
        title: A string representing the title of the movie.
        storyline: A short description of the movie.
        poster_image_url: A url to an image file of the poster of the movie
        trailer_youtube_url: A url to a youtube video of the trailer of the movie.
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube