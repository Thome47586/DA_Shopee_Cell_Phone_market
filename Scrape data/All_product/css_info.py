import json
from selenium import webdriver

#browser = webdriver.Chrome(executable_path='./chromedriver')

def get_info_css(name_check):
    
    try:
        
        jsonscripts = browser.find_elements_by_css_selector('[type="application/ld+json"]')
        for i in jsonscripts:
            tmp = i.get_attribute('innerHTML') 
            jsonproduct = json.loads(tmp) # Convert to json data
            print(jsonproduct.keys())
            if 'name' in jsonproduct.keys() and 'aggregateRating' in jsonproduct.keys():
                if name_check == jsonproduct['name']:
                    print(name_check)
                    print(jsonproduct['name'])
                    rating = jsonproduct['aggregateRating']['ratingValue']
                    # print(rating)
                    #rating_count = jsonproduct['aggregateRating']['ratingCount']
                    # print(rating_count)
                    return rating #rating_count

    except Exception as e:
        print("Have and error", e)
        pass