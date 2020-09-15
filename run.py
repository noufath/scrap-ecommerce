import requests
import json
from bs4 import BeautifulSoup

session = requests.Session()


def login():
    dt_login = {
        'username': 'user',
        'password': 'user12345'
    }
    post_response = session.post("http://localhost:5000/login", data=dt_login)
    soup = BeautifulSoup(post_response.text, "html5lib")
    page_item = soup.find_all('li', attrs={'class': 'page-item'})
    tot_page = len(page_item) - 2
    return tot_page


def get_url(page, catch_urls=[]):
    print('process... url page {}'.format(page))
    par_data = {
        'page': page
    }
    get_response = session.get("http://localhost:5000", params=par_data)

    # f_login = open('./resp.html', 'w+')
    # f_login.write(get_response.text)
    # f_login.close()

    soup = BeautifulSoup(get_response.text, "html5lib")

    # After download html file from request, it's can use for scrap in development so, we don't need to do request every
    # time we run program
    # soup = BeautifulSoup(open('./resp.html'), "html5lib")

    titles = soup.find_all('h4', attrs={'class': 'card-title'})

    for title in titles:
        catch_url = title.find('a')['href']
        catch_urls.append(catch_url)

    return catch_urls


def get_detail(url):
    print('getting detail....')
    detail_response = session.get('http://localhost:5000'+url)

    # f_login = open('./resp.html', 'w+')
    # f_login.write(detail_response.text)
    # f_login.close()

    soup = BeautifulSoup(detail_response.text, 'html5lib')
    title = soup.find('title').text.strip()
    price = soup.find('h4', attrs={'class': 'card-price'}).text.strip()
    stock = soup.find('span', attrs={'class': 'card-stock'}).text.strip().replace('stock: ', '')
    category = soup.find('span', attrs={'class': 'card-category'}).text.strip().replace('category: ', '')
    description = soup.find('p', attrs={'class': 'card-text'}).text.strip().replace('Description: ', '')

    dict_data = {
        'title': title,
        'price': price,
        'stock': stock,
        'category': category,
        'description': description
    }

    with open('./result/{}.json'.format(url.replace('/', '')), 'w+') as outfile:
        json.dump(dict_data, outfile)


def run(urls=[]):
    pages = login()

    # for i in range(pages):
    #     page = i + 1
    #     urls = urls + get_url(page)
    #
    #     with open('urls.json', 'w+') as outfile:
    #         json.dump(urls, outfile)
    # After json file created we can command line getting url request and use json file directly

    # with open('urls.json') as json_file:
    #    all_url = json.load(json_file)

    # for url in all_url:
    #    get_detail(url)

    get_detail('/mamypoko-good-night-pants-xxl-28-girls')


if __name__ == '__main__':
    run()
