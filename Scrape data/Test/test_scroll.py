from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import json
import info_shop


# main_url = 'https://shopee.vn/N%E1%BA%AFp-l%C6%B0ng-Nokia-6.1-plus-Nokia-X6-2018-i.183997654.3800627616?position=962'



# driver = webdriver.Chrome(executable_path='/Users/Thome/Desktop/CoderSchool/Shopee_Phone_EDA/chromedriver')


# driver.get(main_url)
# driver.execute_script("window.scrollBy(0, 5000)", "")
# time.sleep(3)



data_2 = []
i =  519
while i < len(list_url):
        i += 1
        print(f'Number: {i}')
        print(list_url[i]) # Link 0

        # Initialize webdriver as browser
        driver = webdriver.Chrome(
                                executable_path='/Users/Thome/Desktop/CoderSchool/Shopee_Phone_EDA/chromedriver')
        
        driver.get(list_url[i])
        driver.execute_script("window.scrollBy(0, 5000)", "")
        time.sleep(5)


        # All content in page
        element_product_2 = driver.find_element_by_id('main')
        # Content json
        css_2 = driver.find_elements_by_css_selector('[type="application/ld+json"]')
        content_css_2 = []
        for content in css_2:
            tmp = content.get_attribute('innerHTML')
            json_content =  json.loads(tmp)
            content_css_2.append(json_content)
        try:
            # Collect data
            data_shop_2 = info_shop.get_info_shop(element_product_2, content_css_2[1])
            data_2.append(data_shop_2)
            driver.close()
        except: continue
        
        if i == 1040:
            break

df2 = pd.DataFrame(data=data_2, columns=data_2[0].keys())
df2.to_csv('detailed_data_2.csv')


def collect_data(i):
        data_2 = []
        i += 1
        print(f'Number: {i}')
        print(list_url[i]) # Link 0

        # Initialize webdriver as browser
        driver = webdriver.Chrome(executable_path='/Users/Thome/Desktop/CoderSchool/Shopee_Phone_EDA/chromedriver')
        
        driver.get(list_url[i])
        driver.execute_script("window.scrollBy(0, 5000)", "")
        time.sleep(5)


        # All content in page
        element_product_2 = driver.find_element_by_id('main')
        # Content json
        css_2 = driver.find_elements_by_css_selector('[type="application/ld+json"]')
        content_css_2 = []
        for content in css_2:
            tmp = content.get_attribute('innerHTML')
            json_content =  json.loads(tmp)
            content_css_2.append(json_content)
        try:
            # Collect data
            data_shop_2 = info_shop.get_info_shop(element_product_2, content_css_2[1])
            data_2.append(data_shop_2)
            driver.close()
        except: 
            continue
        
        if i == 1040:
            break
    return data_2






    