class UserInterface:
    def initial_data(self):
        print('Действия с фильмами')
        print('1 - добавление фильма\n'
              '2 - каталог фильмов\n'
              '3 - просмотр определенного фильма\n'
              '4 - удаление фильма\n'
              'exit - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer

    def add_movie(self):
        dict_movie = {
            'название': None,
            'жанр': None,
            'режиссер': None,
            'год выпуска': None,
            'длительность': None,
            'студия': None,
            'актеры': None,
        }

        for key in dict_movie:
            dict_movie[key] = input(f'Введите {key} фильма: ')
        return dict_movie

    def show_all_movies(self, movies):
        for i, movie in enumerate(movies, start=1):
            print(f'{i}.{movie}')

    def get_user_movie(self):
        user_movie = input('Введите название фильма: ')
        return user_movie

    def show_single_movie(self, film):
        for key in film:
            print(f'{key} фильма - {film[key]}')

    def remove_single_movie(self, title):
        print(f'Фильм "{title}" был удален')
