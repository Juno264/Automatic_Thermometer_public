from discordwebhook import Discord
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from tokenize import String
from typing_extensions import Self
from webdriver_manager.chrome import ChromeDriverManager


#Discord用のwebhookを追加
discord = Discord(url="WEDHOOK")

#userdataクラス
class Userdata:
    def __init__(self, name, phonenumber, password):
        self.name: String = name
        self.phonenumber: int = phonenumber
        self.password: String = password


#ユーザー情報
user0 = Userdata("NAME1",PHONENUMBER1,"PASS1")
user1 = Userdata("NAME2",PHONENUMBER1,"PASS2")
...

all_users = [user0,user1,...]

# リンク
url = 'https://web.leber.jp/index.html'

# ブラウザを立ち上げないようにオプションを指定
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=880x996")
options.add_argument("--no-sandbox")

#全ユーザーの検温を送信
for i in all_users:

    tel = i.phonenumber
    password = i.password
    print(i.name,":",tel,":",password)
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
    print("電話番を入力して次へを選択")
    sleep(1)
    title = browser.title
    print(title)

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
    # sleep(1)

    #体温２
    dropdown = browser.find_element(By.XPATH,('/html/body/div[4]/div/div[2]/div/div/div/div/div[1]/div[3]/select'))
    select = Select(dropdown)
    select.select_by_index(26)

    #体温３
    browser.find_element(By.XPATH,('/html/body/div[4]/div/div[2]/div/div/div/div/div[1]/div[5]')).click()
    print("体温を回答")
    # sleep(1)

    #時間１
    browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div')).click()
    # sleep(1)

    #時間２
    dropdown = browser.find_element(By.XPATH,('/html/body/div[4]/div/div[2]/div/div/div/div/div[1]/div[3]/select'))
    select = Select(dropdown)
    select.select_by_index(6)
    # sleep(1)

    #時間３
    browser.find_element(By.XPATH,('/html/body/div[4]/div/div[2]/div/div/div/div/div[1]/div[5]')).click()
    print("時間を回答")
    # sleep(1)

    #体調１
    browser.find_element(By.XPATH,('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div[3]/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div')).click()
    # sleep(1)

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
    
    #discordで報告
    discord.post(content=i.name+"の検温データを送信しました")
