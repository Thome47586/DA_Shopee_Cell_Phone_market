from selenium import webdriver
import time
import single_info

# num_max_page = 99
# main_url = 'https://shopee.vn/%C4%90i%E1%BB%87n-tho%E1%BA%A1i-cat.11036030.11036031?page=0&sortBy=sales'



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



######### Collect all url ###############

def collect_all_url(main_url, max_page=0):

    products = []

    page_n = 0
    page_url = main_url.replace('page=0', f'page={page_n}')
    product_list = get_product_info_singel_page(page_url)

    while len(product_list)>0:
        print(product_list)
        products.extend(product_list)
        page_n += 1

        stop_flag = False if max_page <= 0 else page_n > max_page # For stopping the scrape according to max_page
        if stop_flag:
            break

        page_url = main_url.replace('page=0', f'page={page_n}')
        product_list = get_product_info_singel_page(page_url)
    
    return products