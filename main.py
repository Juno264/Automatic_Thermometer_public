from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from tokenize import String
from typing_extensions import Self
from webdriver_manager.chrome import ChromeDriverManager

# リンク
url = 'https://web.leber.jp/index.html'

# ブラウザを立ち上げないようにオプションを指定
options = webdriver.ChromeOptions()
options.add_argument("--headless") #表で起動するかどうかテストのときは先頭に#つけてコメントアウトして
options.add_argument("--disable-gpu")
options.add_argument("--window-size=880x996")
options.add_argument("--no-sandbox")

#検温を送信
tel = 電話番号
password = "パスワード"
# ブラウザを生成
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
browser.get(url)
print("アクセス成功")
sleep(4)

# ログイン画面に遷移
element = browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div'))
element.click()
print("ログインを選択")
sleep(1)
title = browser.title
print(title)

# 電話番号を入力
browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/input')).send_keys(tel)
browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div')).click()
print("電話番号を入力して次へを選択")
sleep(1)

# パスワードを入力
browser.find_element(By.XPATH,('//input[@type="password"]')).send_keys(password)
browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div')).click()
print("パスワードを入力、ログインを選択")
sleep(5)

# 体温チェックを選択
browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]')).click()
print("体温チェックを選択した")

# ユーザーを選択
browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]')).click()
print("ユーザーを選択")
sleep(1)

#体温１
browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/div')).click()

#体温２
dropdown = browser.find_element(By.XPATH,('/html/body/div[4]/div/div[2]/div/div/div/div/div[1]/div[3]/select'))
select = Select(dropdown)
select.select_by_index(26)#36.6度

#体温３
browser.find_element(By.XPATH,('/html/body/div[4]/div/div[2]/div/div/div/div/div[1]/div[5]')).click()
print("体温を回答")

#時間１
browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div')).click()

#時間２
dropdown = browser.find_element(By.XPATH,('/html/body/div[4]/div/div[2]/div/div/div/div/div[1]/div[3]/select'))
select = Select(dropdown)
select.select_by_index(6)#午前６時

#時間３
browser.find_element(By.XPATH,('/html/body/div[4]/div/div[2]/div/div/div/div/div[1]/div[5]')).click()
print("時間を回答")

#体調１
browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div[3]/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div')).click()

#体調２
browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div[3]/div[2]/div/div/div[2]/div/div')).click()
print("体調を回答")
sleep(2)

#回答を送信
browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/div')).click()
sleep(1)

# 確認用text
print(browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div')).text)

# 閉じる
browser.close()
