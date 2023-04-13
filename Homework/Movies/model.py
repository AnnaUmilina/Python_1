class Movie:
    def __init__(self, title, genre, director, year, time, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.time = time
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f'{self.title}, {self.year}'


class MovieModel:
    def __init__(self):
        self.films = {}

    def add_film(self, dict_movie):
        film = Movie(*dict_movie.values())
        self.films[film.title] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, movie_title):
        film = self.films[movie_title]
        dict_film = {
            'название': film.title,
            'жанр': film.genre,
            'режиссер': film.director,
            'год выпуска': film.year,
            'длительность': film.time,
            'студия': film.studio,
            'актеры': film.actors,
        }
        return dict_film

    def remove_film(self,movie_title):
        return self.films.pop(movie_title)
