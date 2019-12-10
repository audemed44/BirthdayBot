from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time, json
from datetime import date

def wish_birthday(birthday_boy, message):
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=chrome-data")
    driver = webdriver.Chrome('resources\\chromedriver.exe',options=chrome_options)

    try:
        driver.get('https://web.whatsapp.com')  
        wait = WebDriverWait(driver, 60) 
        target = '\"'+birthday_boy+'\"'
        string = message
        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
        group_title.click()
        x_arg2 = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        input_box = driver.find_element_by_xpath(x_arg2)
        input_box.send_keys(string) 
        input_box.send_keys(Keys.ENTER)
        time.sleep(1) 

    except Exception as error: 
        print(error)

    finally:
        driver.quit()

with open('birthdays.json') as birthdays_json:
    birthdays = json.load(birthdays_json)

today = date.today()
day = today.day
month = today.month
today_str = str(day)+'-'+str(month)

for birthday in birthdays:
    if birthdays[birthday]["Birthday"] == today_str:
        message = birthdays[birthday]["Message"]
        wish_birthday(birthday,message)


