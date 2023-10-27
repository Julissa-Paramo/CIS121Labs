# TODO: Import Artist from Artist.py
from Artist import Artist

class Artwork:
    def __init__(self, title='unknown', year_created=-1, artist=Artist()):
        self.title = title
        self.year_created = year_created
        self.artist = artist
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)

    def print_info(self):
        self.artist.print_info()
        print(f'Title: {self.title}, {self.year_created}')
