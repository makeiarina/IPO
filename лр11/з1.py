class MusicCollection:
    """
    Класс, представляющий музыкальную коллекцию.

    Атрибуты:
    - collection_name (str): Название музыкальной коллекции.
    - artist (str): Имя исполнителя.
    - year (int): Год выпуска альбома.
    - genre (str): Жанр музыки.
    - num_tracks (int): Количество треков в альбоме.
    - duration (float): Продолжительность альбома в минутах.

    Методы:
    - get_collection_info(): Выводит на экран информацию о музыкальной коллекции.
    - play_track(track_number: int): Воспроизводит трек с указанным номером.
    - increase_duration(additional_duration: float): Увеличивает продолжительность альбома на указанное значение.
    - change_artist(new_artist: str): Изменяет имя исполнителя.
    """

    def __init__(self, collection_name, artist, year, genre, num_tracks, duration):
        self.collection_name = collection_name
        self.artist = artist
        self.year = year
        self.genre = genre
        self.num_tracks = num_tracks
        self.duration = duration

    def get_collection_info(self):
        """Выводит на экран информацию о музыкальной коллекции."""
        print(f"Название коллекции: {self.collection_name}")
        print(f"Исполнитель: {self.artist}")
        print(f"Год выпуска альбома: {self.year}")
        print(f"Жанр музыки: {self.genre}")
        print(f"Количество треков: {self.num_tracks}")
        print(f"Продолжительность: {self.duration} минут")

    def play_track(self, track_number):
        """Воспроизводит трек с указанным номером."""
        if track_number < 1 or track_number > self.num_tracks:
            print("Ошибка: некорректный номер трека")
        else:
            print(f"Воспроизводится трек номер {track_number}")

    def increase_duration(self, additional_duration):
        """Увеличивает продолжительность альбома на указанное значение."""
        if additional_duration <= 0:
            print("Ошибка: некорректное значение длительности")
        else:
            self.duration += additional_duration
            print(f"Продолжительность альбома увеличена на {additional_duration} минут")

    def change_artist(self, new_artist):
        """Изменяет имя исполнителя."""
        self.artist = new_artist
        print(f"Новый исполнитель: {self.artist}")

# Создание экземпляров класса MusicCollection и инициализация значениями
collection1 = MusicCollection("Best Hits", "Queen", 1981, "Rock", 12, 55.2)
collection2 = MusicCollection("Greatest Hits", "The Beatles", 1967, "Rock", 20, 65.8)
collection3 = MusicCollection("Top 40", "Taylor Swift", 2020, "Pop", 14, 48.3)
collection4 = MusicCollection("Classic Collection", "Mozart", 1770, "Classical", 8, 40.1)
collection5 = MusicCollection("Jazz Standards", "Louis Armstrong", 1950, "Jazz", 10, 42.7)

# Вывод документации класса
print(help(MusicCollection))

# Вызов методов класса
collection1.get_collection_info()
collection2.play_track(5)
collection3.increase_duration(10.5)
collection4.change_artist("Beethoven")