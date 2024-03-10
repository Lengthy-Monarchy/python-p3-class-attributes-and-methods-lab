class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

# Test the Song class
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
drake_song = Song("In My Feelings", "Drake", "Rap")
beyonce_song = Song("Single Ladies", "Beyonce", "Pop")

print(Song.count)  # Output: 3
print(Song.genres)  # Output: ['Rap', 'Pop']
print(Song.artists)  # Output: ['Jay-Z', 'Drake', 'Beyonce']
print(Song.genre_count)  # Output: {'Rap': 2, 'Pop': 1}
print(Song.artist_count)  # Output: {'Jay-Z': 1, 'Drake': 1, 'Beyonce': 1}
