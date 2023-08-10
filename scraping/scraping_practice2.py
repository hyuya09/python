import requests
from bs4 import BeautifulSoup

#ページの取得
url = 'https://scraping-for-beginner.herokuapp.com/udemy'
res = requests.get(url)

#ページ情報をhtmlにする
soup = BeautifulSoup(res.text, 'html.parser')

#<p>の取得
# print(soup.find_all('p')[0])
# print(soup.find('p'))
# print(soup.text)

#テキストの取得
subscribers = soup.find_all('p', attrs = {'class': 'subscribers'})[0]
n_subscribers = int(subscribers.text.split('：')[1])
print(n_subscribers)

reviews = soup.find_all('p', attrs = {'class': 'reviews'})[0]
n_reviews = int(reviews.text.split('：')[1])
print(n_reviews)

soup.select_one('.subscribers')
soup.select_one('.reviews')