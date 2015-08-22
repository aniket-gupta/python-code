import webbrowser


class Movie(object):

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailor_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailor_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
