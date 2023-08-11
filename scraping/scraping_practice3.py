import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://scraping-for-beginner.herokuapp.com/ranking/'
res = requests.get(url)

soup = BeautifulSoup(res.content, 'html.parser')

# #1つの観光地情報を取得
# #観光地名
# spots = soup.find_all('div', attrs = {'u_areaListRankingBox'})
# spot = spots[0]
# spot_name = spot.find('div', attrs = {'u_title'})
# # spot_name.find('span', attrs = {'badge'}).extract() #.extract()→指定した部分を抜き取る
# spot_name = spot_name.text.replace('\n', '')
# print(spot_name)

# #評点
# eval_num = spot.find('div', attrs = {'u_rankBox'})
# eval_num = float(eval_num.text)
# print(eval_num)

# categoryItems = spot.find('div', attrs = {'u_categoryTipsItem'})
# categoryItems = categoryItems.find_all('dl')
# categoryItem = categoryItems[0]
# category = categoryItem.dt.text
# rank = float(categoryItem.span.text)
# print(category)

# details = {}
# # categoryItem = categoryItems[0]
# for categoryItem in categoryItems:
#   category = categoryItem.dt.text
#   rank = float(categoryItem.span.text)

#   details[category] = rank
# print(details)

# datum = details
# datum['観光地名'] = spot_name
# datum['評点'] = eval_num
# print(datum)


#一度に全ての情報を取得
data = []

spots = soup.find_all('div', attrs = {'u_areaListRankingBox'})
for spot in spots:
  spot_name = spot.find('div', attrs = {'u_title'})
  spot_name.find('span', attrs = {'badge'}).extract() #.extract()→指定した部分を抜き取る
  spot_name = spot_name.text.replace('\n', '')

  eval_num = spot.find('div', attrs = {'u_rankBox'})
  eval_num = float(eval_num.text)

  categoryItems = spot.find('div', attrs = {'u_categoryTipsItem'})
  categoryItems = categoryItems.find_all('dl')
  categoryItem = categoryItems[0]
  category = categoryItem.dt.text
  rank = float(categoryItem.span.text)

  details = {}
  # categoryItem = categoryItems[0]
  for categoryItem in categoryItems:
    category = categoryItem.dt.text
    rank = float(categoryItem.span.text)

    #keyvalueへの追加
    details[category] = rank

  datum = details
  datum['観光地名'] = spot_name
  datum['評点'] = eval_num
  data.append(datum)
# print(data)

df = pd.DataFrame(data)
df = df[['観光地名', '評点', 'アクセス', '人混みの多さ', '景色', '楽しさ']]
df.to_csv('観光地情報.csv', index = False)
# print(df)


