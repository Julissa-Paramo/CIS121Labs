
from Artist import Artist

class Artwork:
    def __init__(self, title='unknown', year_created=-1, artist=Artist()):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        self.artist.print_info()
        print(f'Title: {self.title}, {self.year_created}')
