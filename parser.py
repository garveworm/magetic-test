import requests
from bs4 import BeautifulSoup


class Parser(object):
    """
    Parse user to retrieve infromation from google play games page
    expects url as first argument
    """

    def __init__(self, url, *args, **kwargs):
        self.url = url
        self.games = {}

    def get_html(self, url):
        """
        method used to make get request and parse page html with BeautifulSoup
        :param url:
        :return: HTML page content
        """
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def get_categories(self, soup):
        """
        method used to retrieve game categories fromm HTML
        :param soup: HTML content of the page(created with BeautifulSoup)
        :return: list of categories
        """
        categories = soup.find_all("div", class_="id-cluster-container cluster-container cards-transition-enabled")
        return categories

    def parse_games(self, game):
        """
        Parse game object
        :param game:
        :return: game title
        """
        game_title = game.select("a.title")
        return game_title[0].text

    def parse_category(self, category):
        """
        method user to parse games category and retrieve title
        :param category: single category object
        :return: category title
        """
        category_title = category.select("a.title-link")
        title = ""
        try:
            title = category_title[0].text
        except IndexError:
            title = "No title"
        return title


    def parse(self):
        """
        Main method, calls other methods and parses page
        :return: dict of category and game names
        """
        html = self.get_html(self.url)
        categories = self.get_categories(html)

        for cat in categories:
            # get name of every category
            category_name = self.parse_category(cat)
            print(category_name)

            # get name of games in category
            games = cat.find_all("div", class_="card-content id-track-click id-track-impression")
            games_names_list = []
            for game in games:
                game_name = self.parse_games(game)
                games_names_list.append(game_name)

            #update games dict with obtained values
            self.games[category_name] = games_names_list

        return self.games

    def print_games(self):
        for key, values in self.games.items():
            for value in values:
                print(f'{key}/{value.strip()}\n')


if __name__ == '__main__':
    google_play_parser = Parser('https://play.google.com/store/apps/category/GAME')
    google_play_parser.parse()
    google_play_parser.print_games()

