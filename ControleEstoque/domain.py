class Musician:
    def __init__(self, first_name, last_name, instrument):
        self.first_name = first_name
        self.last_name = last_name
        self.instrument = instrument

class Album:
    def __init__(self, artist, name, release_date, num_stars):
        self.artist = artist
        self.name = name
        self.release_date = release_date
        self.num_stars = num_stars

        #camada de dominio