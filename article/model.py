class Article:
    def __init__(self, title, author, page, description):
        self.title = title
        self.author = author
        self.page = page
        self.description = description

    def __str__(self):
        return f'{self.title} ({self.author})'


class ArticleModel:
    def __init__(self):
        self.articles = {}

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_article(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            "название": article.title,
            "автор": article.author,
            "количество страниц": article.page,
            "описание": article.description
        }
        return dict_article
