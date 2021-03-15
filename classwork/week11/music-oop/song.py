class Song():
    def __init__(self, name="unknown", genre="unknown"):
        self._name = name
        self._genre = genre

    def get_name(self):
        return self._name

    def get_genre(self):
        return self._genre

    def set_name(self, name):
        self._name = name

    def set_genre(self, genre):
        self._genre = genre
