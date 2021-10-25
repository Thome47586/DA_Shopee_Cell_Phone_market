from selenium import webdriver
import pandas as pd
import single_info
import json
import time




data = []
page_n = 0
max_page = 99
main_url = 'https://shopee.vn/%C4%90i%E1%BB%87n-tho%E1%BA%A1i-cat.11036030.11036031?page=0&sortBy=sales'

''' Open and Crawl'''
while page_n >= 0:

    # 3. Get url
    url = main_url.replace('page=0', f'page={page_n}')

    # 1. browser declaration
    browser = webdriver.Chrome(executable_path='/Users/Thome/Desktop/CoderSchool/Shopee_Phone_EDA/chromedriver')
    # 4. Open url
    browser.get(url)
    
    # 5. scroll and load page
    browser.execute_script("window.scrollBy(0, 1000)", "")
    time.sleep(3)

    browser.execute_script("window.scrollBy(0, 1100)", "")
    time.sleep(3)

    browser.execute_script("window.scrollBy(0, 1100)", "")
    time.sleep(3)    

    browser.execute_script("window.scrollBy(0, 1000)", "")
    time.sleep(3)   
    
    # 6. Count products in one page
    # Output is a list selenium all products
    all_products = browser.find_elements_by_class_name('col-xs-2-4')
    print(f'Found {len(all_products)} products')

    # get list info from CSS
    css = browser.find_elements_by_css_selector('[type="application/ld+json"]')
    print(f'Css: {len(css)}')
    json_product = []
    for i in range(2, len(css)):
        tmp = css[i].get_attribute('innerHTML')
        # convert to json data
        json_info = json.loads(tmp)
        json_product.append(json_info)

        # 7. Get single info product
        #for product in all_products:
    for i in range(len(all_products)):
        data_single_product = single_info.get_single_info_product(all_products[i], json_product[i])
        data.append(data_single_product)
            # pass
            # break
            # Continue
        #print(f'Number of product: {all_products.index(product)}')
            

    #  Next page
    print(f'Number of pages: {page_n}')
    page_n += 1
    if page_n == max_page:
        browser.close()
        break

# Save file
df = pd.DataFrame(data=data, columns=data[0].keys())
df.to_csv('shopee_phone.csv')

