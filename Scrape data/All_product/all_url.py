import single_page

# num_max_page = 99
# main_url = 'https://shopee.vn/%C4%90i%E1%BB%87n-tho%E1%BA%A1i-cat.11036030.11036031?page=0&sortBy=sales'


def collect_all_url(main_url, max_page=0):

    products = []

    page_n = 0
    page_url = main_url.replace('page=0', f'page={page_n}')
    product_list = single_page.get_product_info_singel_page(page_url)

    while len(product_list)>0:
        print(product_list)
        products.extend(product_list)
        page_n += 1

        stop_flag = False if max_page <= 0 else page_n > max_page # For stopping the scrape according to max_page
        if stop_flag:
            break

        page_url = main_url.replace('page=0', f'page={page_n}')
        product_list = single_page.get_product_info_singel_page(page_url)
    
    return products