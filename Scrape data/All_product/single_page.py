# import browser_driver
from selenium import webdriver
import time
import single_info


def get_product_info_singel_page(page_url):

    data = []
    print(page_url)

    # call web driver    
    browser = webdriver.Chrome(executable_path='./chromedriver')

    browser.get(page_url) # Use the driver to get info from the product page
    time.sleep(5)

    # FIND ALL PRODUCT ITEMS
    all_products = browser.find_elements_by_class_name('col-xs-2-4')
    print(f'Found {len(all_products)} products')

    
    for element in all_products:
            product_dict = single_info.get_single_info_product(element)

            data.append(product_dict)
    


    return data

