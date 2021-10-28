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




data_scrape = []
i =  -1
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
            element_product = driver.find_element_by_id('main')
            # Content json
            css = driver.find_elements_by_css_selector('[type="application/ld+json"]')
            content_css = []
            for content in css:
                tmp = content.get_attribute('innerHTML')
                json_content =  json.loads(tmp)
                content_css.append(json_content)
        except NoSuchElementException:
            pass
        
        try:
            # Collect data
            data_shop_2078 = info_shop.get_info_shop(element_product, content_css[1], list_url[i])
            data_scrape.append(data_shop_2078)
            driver.close()
        except: continue

        if i >= 2077  :
            break

df = pd.DataFrame(data=data_scrape, columns=data_scrape[0].keys())
df.to_csv('data.csv')
