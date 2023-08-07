from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

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
