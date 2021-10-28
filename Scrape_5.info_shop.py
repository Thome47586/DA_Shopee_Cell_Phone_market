from selenium.common.exceptions import NoSuchElementException


#################
### FUNCTIONS ###
#################

# Function to extract product info from the necessary html and json tags
def get_info_shop(element_product, content_css_1, url):
    data_detail_product = {
         'product_url': '',
         'name_product':'',
         'rating_product':'',
         'rating_count_product':'',
         'quantity_5_star': '',
         'quantity_4_star': '',
         'quantity_3_star': '',
         'quantity_2_star': '',
         'quantity_1_star': '',
         'count_cmt': '',
         'images_video': '',
         'sold_out':'',
         'low_price':'',
         'hight_price':'',
         'price':'',
         'inventory':'',
         'return_7_days': '',
         'authentic':'',
         'freeship':'',
         'shopee_guaranteed': '',
         'company':'',
         'shop_name': '',
         'shopee_mall':'',
         'shop_total_review':'',
         'total_products':'',
         'response_rate':'',
         'time_response':'',
         'years_ex': '',
         'follower': '',
         }

    # product_url
    try:
        data_detail_product['product_url'] = url
    except:
        pass
    
    # name
    try:
        name = element_product.find_element_by_class_name('attM6y')
        data_detail_product['name_product'] = name.text
    except:
        pass

    # rating and raing count of product
    try:
        data_detail_product['rating_product'] = content_css_1['aggregateRating']['ratingValue']
        data_detail_product['rating_count_product'] = content_css_1['aggregateRating']['ratingCount']
    except:
        pass
    
    # Quantity stars:
    try:
        all_rating = element_product.find_elements_by_class_name('product-rating-overview__filters')

        data_detail_product['quantity_5_star'] = all_rating[0].text.split(')')[0].replace('(', '').strip('Tất Cả5 Sao')
        data_detail_product['quantity_4_star'] = all_rating[0].text.split(')')[1].replace('4 Sao (', '')
        data_detail_product['quantity_4_star'] = all_rating[0].text.split(')')[2].replace('3 Sao (', '')
        data_detail_product['quantity_4_star'] = all_rating[0].text.split(')')[3].replace('2 Sao (', '')
        data_detail_product['quantity_4_star'] = all_rating[0].text.split(')')[4].replace('1 Sao (', '')
        data_detail_product['count_cmt']       = all_rating[0].text.split(')')[5].strip('Có Bình Luận (')
        data_detail_product['images_video']    = all_rating[0].text.split(')')[6].strip('Có Hình Ảnh / Video (')
    except:
        pass

    # sold_out
    try:
        data_detail_product['sold_out'] = element_product.find_element_by_class_name('aca9MM').text
    except:
        pass

    # low_price, hight_price and price
    try:
        data_detail_product['hight_price'] = content_css_1['offers']['lowPrice']
        data_detail_product['low_price']  = content_css_1['offers']['highPrice']
    except:
        pass
    
    try:
        data_detail_product['price'] = content_css_1['offers']['price']
    except:
        pass

    # inventory
    try:
        inventory = element_product.find_element_by_class_name('product-briefing')
        inventory = inventory.find_element_by_class_name('flex.items-center._90fTvx')
        
        data_detail_product['inventory'] = inventory.text.split('\n')[-1].strip(' sản phẩm có sẵn')
    except:
        pass
    
    # return_7_days, authentic, freeship, shopee_guaranteed
    try:
        return_authen_freeship = element_product.find_element_by_class_name('_3evuG0')
        data_detail_product['return_7_days'] = return_authen_freeship.text.split('\n')[0]
        data_detail_product['authentic']     = return_authen_freeship.text.split('\n')[1]
        data_detail_product['freeship']      = return_authen_freeship.text.split('\n')[2]
    except:
        guaranteed             = element_product.find_element_by_class_name('flex-auto.flex-column._1rcM18')
        data_detail_product['shopee_guaranteed'] = guaranteed.text.split('\n')[-1]


    # shop_name
    try:
        data_detail_product['shop_name'] = element_product.find_element_by_class_name('_3uf2ae').text
    except:
        pass

    # company
    try:
       data_detail_product['company'] = content_css_1['offers']['seller']['name']
    except:
        pass

    # shopee_mall
    try:
        data_detail_product['shopee_mall'] = bool(element_product.find_element_by_class_name('qutJvu'))
    except:
        data_detail_product['shopee_mall'] = False

    # shop_total_review, total_products, response_rate, time_response, years_ex, follower
    try:
       total_info_shop = element_product.find_element_by_class_name('_309kqV').text.split('\n')
       data_detail_product['shop_total_review']   = total_info_shop[1]
       data_detail_product['total_products']      = total_info_shop[3]
       data_detail_product['response_rate']       = total_info_shop[5]
       data_detail_product['time_response']       = total_info_shop[7]
       data_detail_product['years_ex']            = total_info_shop[9]
       data_detail_product['follower']            = total_info_shop[11]
    except:
        pass
    
    return data_detail_product
