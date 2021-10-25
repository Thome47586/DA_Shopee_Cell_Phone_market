from selenium import webdriver

browser = None
# Function to (re)start driver
def start_browser(force_restart=False):
    global browser
    
    if browser is not None:
        if force_restart:
            browser.close()
        else:
            raise RuntimeError('ERROR: cannot overwrite an active driver. Please close the driver before restarting.')

    browser = webdriver.Chrome(executable_path='./chromedriver')

# Wrapper to close driver if its created
def close_browser():
    global browser
    if browser is not None:
        browser.close()
    browser = None