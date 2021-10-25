from selenium import webdriver
import time
import all_url
import pandas as pd
import single_info
import json


######################
### START SCRAPING ###
######################


num_max_page = 2 #99
main_url = 'https://shopee.vn/%C4%90i%E1%BB%87n-tho%E1%BA%A1i-cat.11036030.11036031?page=0&sortBy=sales'

data = []
page_n = 0
while page_n >= 0:
    page_url = main_url.replace('page=0', f'page={page_n}')

    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get(page_url) 
    time.sleep(5)


    # # function css
    # def get_info_css(name_check):
    #     try:
    #         jsonscripts = browser.find_elements_by_css_selector('[type="application/ld+json"]')
    #         for i in jsonscripts:
    #             tmp = i.get_attribute('innerHTML') 
    #             jsonproduct = json.loads(tmp) # Convert to json data
    #             print(jsonproduct.keys())
    #             if 'name' in jsonproduct.keys() and 'aggregateRating' in jsonproduct.keys():
    #                 if name_check == jsonproduct['name']:
    #                     print(name_check)
    #                     print(jsonproduct['name'])
    #                     rating = jsonproduct['aggregateRating']['ratingValue']
    #                     # print(rating)
    #                     #rating_count = jsonproduct['aggregateRating']['ratingCount']
    #                     # print(rating_count)
    #                     return rating #rating_count

    #     except Exception as e:
    #         print("Have and error", e)
    #         pass


    # All data by class
    print('tới đây')
    all_products = browser.find_elements_by_class_name('col-xs-2-4')
    print(f'Found {len(all_products)} products')
    
    for element in all_products:
      
        product_dict = single_info.get_single_info_product(element)
        # Product_dict all data in a page
        data.append(product_dict)
     
    
    # Next page
    if page_n <= 2:

        page_n += 1
        print(page_n)
    else:
        browser.close()
        break   

df = pd.DataFrame(data=data, columns=data[0].keys())
df.to_csv('shopee_phone_3.csv')

