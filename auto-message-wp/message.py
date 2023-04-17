from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import schedule
import random

def get_random_message(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        messages = file.readlines()
    return random.choice(messages).strip()

def send_message(phone_number, message):
    search_box_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p'
    search_box = driver.find_element(By.XPATH, search_box_xpath)
    search_box.send_keys(phone_number)
    search_box.send_keys(Keys.ENTER)

    message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    message_box = driver.find_element(By.XPATH, message_box_xpath)
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

s = Service("path/to/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://web.whatsapp.com/")
time.sleep(10)

phone_number = "+9055555555" #Mesaj göndermek istediğin telefon numarasını gir.

def send_random_message():
    message = get_random_message("auto-message-wp/messages.txt")
    send_message(phone_number, message)

# Her saat başı rastgele bir mesaj gönderme işlemini planlama
schedule.every().hour.at(":00").do(send_random_message)

while True:
    schedule.run_pending()
    time.sleep(60)  # Her 60 saniyede bir planlanmış görevleri kontrol et