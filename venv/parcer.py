from bs4 import BeautifulSoup
import requests

url = 'http://mignews.com/mobile'

page = requests.get(url)
new_news = []
news = []

print(page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')

news = soup.findAll('a', class_='lenta')

for i in range(len(news)):

    if news[i].find('span', class_='time2 time3') is not None:
        new_news.append(news[i].text)

for i in range(len(new_news)):
    print(new_news[i])































