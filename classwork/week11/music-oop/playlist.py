from song import Song


class Playlist():
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)

    def list_song(self, genre=None):
        if genre == None:
            return self._songs

        return_list = []
        for song in self._songs:
            if song.get_genre() == genre:
                return_list.append(song)
        return return_list
