import requests
from bs4 import BeautifulSoup


class GetData:
    def __init__(self, url_name, url_data, url_param, session_opt):
        self.url = url_name
        self.url_data = url_data

