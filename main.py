import requests
import bs4

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

base_url = 'https://habr.com'
url = base_url + '/ru/all/'
KEYWORDS = ['Видеокарты', 'Облачные сервисы', 'Логические игры']

response = requests.get(url, headers=HEADERS)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
# print(articles)
for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__hubs-item")
    hubs = set(hub.text.strip() for hub in hubs)
    # print(hubs)

    for hub in hubs:
        if hub in KEYWORDS:
            href = article.find(class_="tm-article-snippet__title-link").attrs['href']
            link = base_url + href
            title = article.find('h2').find('span').text
            date = article.find('span', class_="tm-article-snippet__datetime-published").text
            result = date + ' - ' + title + ' - ' + link
            print(result)

