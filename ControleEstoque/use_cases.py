class CreateMusician:
    def __init__(self, musician_repository):
        self.musician_repository = musician_repository

    def execute(self, first_name, last_name, instrument):
        musician = Musician(first_name, last_name, instrument)
        self.musician_repository.save(musician)

class CreateAlbum:
    def __init__(self, album_repository):
        self.album_repository = album_repository

    def execute(self, artist, name, release_date, num_stars):
        album = Album(artist, name, release_date, num_stars)
        self.album_repository.save(album)

