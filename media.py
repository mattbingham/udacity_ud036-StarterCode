import webbrowser


class Shared():
    """Shared attributes. currently used for movies, future case for TV"""

    def __init__(self, title, description, image, trailer):
        self.title = title
        self.description = description
        self.image = image
        self.trailer = trailer


class Movie(Shared):
    """This class provides a way to store movie related information"""

    def __init__(self, title, description, image, trailer, length, year):
        Shared.__init__(self, title, description, image, trailer)
        self.length = length
        self.year = year
