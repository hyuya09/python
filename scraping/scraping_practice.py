from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

options = Options()
#CUIで実行(画面が表示されずに実行される)
options.add_argument('--headless') #selenium4は headless = Trueの場合あり

#処理後も画面の表示を維持
options.add_experimental_option('detach', True)

browser = webdriver.Chrome(options=options)

url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)
sleep(3)

#同じidのinputに要素を自動で入力する
elem_username = browser.find_element(By.ID,'username').send_keys('imanishi')
elem_password = browser.find_element(By.ID,'password').send_keys('kouhei')
sleep(1)

#ログインボタンを自動でクリック
elem_login_btn = browser.find_element(By.ID,'login-btn').click()

#テキストの取得
name = browser.find_element(By.ID, 'name').text
company = browser.find_element(By.ID, 'company').text
birthday = browser.find_element(By.ID, 'birthday').text
hobby = browser.find_element(By.ID, 'hobby').text

#テキストの複数取得
elems_th = browser.find_elements(By.TAG_NAME, 'th')
elems_td = browser.find_elements(By.TAG_NAME, 'td')

keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)

values = []
for elem_td in elems_td:
    value = elem_td.text
    values.append(value)


#CSVファイルへ出力
df = pd.DataFrame()
df['項目'] = keys
df['値'] = values
df.to_csv('講師情報.csv', index = False) #index = False->インデックスが必要ない場合