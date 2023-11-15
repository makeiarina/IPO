class MusicCollection:
    def __init__(self, artist, album, num_tracks):
        self._artist = None
        self._album = None
        self._num_tracks = 0
        self._duration = 0
        self.set_artist(artist)
        self.set_album(album)
        self.set_num_tracks(num_tracks)

    def __del__(self):
        print("Деструктор выполнен для", self.get_album())

    def set_artist(self, artist):
        self._artist = artist

    def set_album(self, album):
        self._album = album

    def set_num_tracks(self, num_tracks):
        if num_tracks < 0:
            print("Ошибка: некорректное количество треков")
        else:
            self._num_tracks = num_tracks

    def set_duration(self, duration):
        if duration < 0:
            print("Ошибка: некорректная продолжительность")
        else:
            self._duration = duration

    def get_artist(self):
        return self._artist

    def get_album(self):
        return self._album

    def get_num_tracks(self):
        return self._num_tracks

    def get_duration(self):
        return self._duration


# Создание списка объектов с использованием конструктора
collection_list = []
for _ in range(10):
    artist = input("Введите исполнителя: ")
    album = input("Введите название альбома: ")
    num_tracks = int(input("Введите количество треков: "))
    collection = MusicCollection(artist, album, num_tracks)
    collection_list.append(collection)

# Пример вызова деструктора для каждого элемента списка при завершении программы