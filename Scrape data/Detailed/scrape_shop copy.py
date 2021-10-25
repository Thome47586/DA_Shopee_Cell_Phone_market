from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import info_shop
import json
import time



# Data all phone sold in Shopee
df = pd.read_csv('/Users/Thome/Desktop/CoderSchool/Shopee_Phone_EDA/EDA/shopee_phone_final.csv')

# Collect product url
list_url = list(df['product_url'])
print(len(list_url)) # 2078

options = Options()
options.add_argument('-headless') # we don't want a chrome browser opens, so it will run in the background
options.add_argument("--no-sandbox")
options.add_argument('-disable-dev-shm-usage')
options.add_argument("--disable-extensions")
options.add_argument("--dns-prefetch-disable")
options.add_argument("--disable-gpu")
options.page_load_strategy = 'eager'



######################################################################################################################################################
# 500 - 999
data_1000 = []
i =  499
while i < len(list_url):
        i += 1
        
        print(f'Number: {i}')
        print(list_url[i]) # Link 0

        # Initialize webdriver as browser
        driver = webdriver.Chrome(executable_path='/Users/Thome/Desktop/CoderSchool/Shopee_Phone_EDA/Scrape data/All_product/chromedriver', options=options)
        driver.set_script_timeout(10)
        driver.implicitly_wait(10)
        
        
        driver.get(list_url[i])
        driver.execute_script("window.scrollBy(0, 5000)", "")
        time.sleep(1)
        try:
            # All content in page
            element_product_1000 = driver.find_element_by_id('main')
            # Content json
            css_1000 = driver.find_elements_by_css_selector('[type="application/ld+json"]')
            content_css_1000 = []
            for content in css:
                tmp = content.get_attribute('innerHTML')
                json_content =  json.loads(tmp)
                content_css_1000.append(json_content)
        except NoSuchElementException:
            pass
        
        try:
            print(content_css_1000[1])
            # Collect data
            data_shop_1000 = info_shop.get_info_shop(element_product_1000, content_css_1000[1], list_url[i])
            data_1000.append(data_shop_1000)
            driver.close()
        except: continue

        if i >= 1000  :
            break
print('maybe_end')
df1000 = pd.DataFrame(data=data_1000, columns=data_1000[0].keys())
df1000.to_csv('detailed_data_1000.csv')
print('end')