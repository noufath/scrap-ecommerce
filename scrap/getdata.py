import requests
from bs4 import BeautifulSoup


class GetData:
    def __init__(self, url_name, url_data):
        self.url = url_name
        self.url_data = url_data
        self.get_response = requests.get(self.url)
        self.post_response = requests.post(self.url, self.url_data)

    def scrap_status(self):
        return self.url_response.status_code

    def parsed_html(self):
        return BeautifulSoup(self.url_response.content, 'html.parser')

    def parsed_body(self):
        return self.parsed_html().find('body')