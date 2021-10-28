from selenium.common.exceptions import NoSuchElementException


#################
### FUNCTIONS ###
#################

# Function to extract product info from the necessary html and json tags
def get_single_info_product(element, json_info):
    d = {'name':'',
         'price_dis':'',
         'price_nondis':'',
         'freeship':'',
         'rating':'',
         'rating_count': '',
         'monthly_sold':'',
         'store_location':'',
         'monthly_event': '',
         'favorite_product':'',
         'shopee_mall':'',
         'discount_tag':'',
         'product_url':'',
         'image':'',
         'ShopDacBiet': '',
         }

    # name
    try:
        name = element.find_element_by_class_name('_10Wbs-')
        d['name'] = name.text
    except NoSuchElementException:
        pass

    # price_dis and price_nondis
    try:
        price_class = element.find_element_by_class_name('_1zR5G3')
        price_dis = price_class.find_elements_by_tag_name('span')[1]
        d['price_dis'] = price_dis.text

        price_nondis = price_class.find_element_by_tag_name('div')
        d['price_nondis'] = price_nondis.text

    except (NoSuchElementException, ValueError):
        pass
    
    # freeship
    try:
        d['freeship'] = bool(element.find_elements_by_class_name('_3etHBT'))
    except NoSuchElementException:
        d['freeship'] = False

    # monthly_sold
    try:
        sold = element.find_element_by_class_name('_2VIlt8')
        d['monthly_sold']  = (sold.text).split(' ')[-1]
    except NoSuchElementException:
        pass

    # store_location
    try:
        shop_location = element.find_element_by_class_name('_1w5FgK')
        d['store_location'] = shop_location.text
    except NoSuchElementException:
        pass
    
    # monthly_event
    try:
        d['monthly_event'] = bool(element.find_element_by_class_name('customized-overlay-image'))
    except NoSuchElementException:
        d['monthly_event'] = False

    # favorite_product
    try:
        favorite_product = element.find_element_by_class_name('_3SZzfE')
        d['favorite_product'] = favorite_product.text
    except NoSuchElementException:
        d['favorite_product'] = None

    # shopee_mall
    try:
       d['shopee_mall'] = bool(element.find_element_by_class_name('_3nVcI9'))
    except NoSuchElementException:
        d['shopee_mall'] = False

    # discount_tag
    try:
       discount = element.find_element_by_class_name('_3yCxz-')
       d['discount_tag'] = discount.text
    except NoSuchElementException:
        d['discount_tag'] = None
    
    # Product url
    try:
        link = element.find_element_by_tag_name('a')
        d['product_url'] = link.get_attribute('href')
    except:
      pass

    # image:
    try:
        image = element.find_element_by_class_name('_3-N5L6._2GchKS')
        d['image'] = image.get_attribute('src')
    except:
        pass

    # ShopDacBiet
    try:
        d['ShopDacBiet'] = bool(element.find_element_by_class_name('WuBb0J'))
    except NoSuchElementException:
        d['ShopDacBiet'] = False

    # Rating
    try:
        d['rating'] = json_info['aggregateRating']['ratingValue']
        d['rating_count'] = json_info['aggregateRating']['ratingCount']

    except Exception as e:
        print('error')
        pass

    return d
