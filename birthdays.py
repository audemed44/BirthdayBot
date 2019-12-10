from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('resources\\chromedriver.exe',options=chrome_options)

try:
    driver.get('https://web.whatsapp.com')  
    wait = WebDriverWait(driver, 60) 
    target = '\"George\"'
    string = "Test "
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
    group_title.click()
    inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
    x_arg2 = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = driver.find_element_by_xpath(x_arg2)

    for i in range(10): 
        string = string + str(i)
        input_box.send_keys(string) 
        input_box.send_keys(Keys.ENTER)
        time.sleep(0.5) 
        string = "Test "

except Exception as error: 
    print(error)

finally:
    driver.quit()
