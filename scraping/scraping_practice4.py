import requests
from bs4 import BeautifulSoup
from PIL import Image
import io

url = 'https://scraping-for-beginner.herokuapp.com/image'
res = requests.get(url)

# soup = BeautifulSoup(res.text, 'html.parser')

# #画像のurlを取得
# img_tag = soup.find('img')
# root_url = 'https://scraping-for-beginner.herokuapp.com'
# img_url = root_url + img_tag['src']

# #画像を保存
# img = Image.open(io.BytesIO(requests.get(img_url).content))
# img.save('img/sample.jpg')

#複数の画像を一度に取得し保存
soup = BeautifulSoup(res.text, 'html.parser')

img_tags = soup.find_all('img')
for i, img_tag in enumerate(img_tags):
  root_url = 'https://scraping-for-beginner.herokuapp.com'
  img_url = root_url + img_tag['src']

  img = Image.open(io.BytesIO(requests.get(img_url).content))
  img.save(f'img/{i}.jpg')