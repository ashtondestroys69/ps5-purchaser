import time
from selenium import webdriver

# For Using Chrome
browser = webdriver.Chrome('/Users/ashto/Desktop/Coding_Portfolio/Projects/Scalper-Bot/chromedriver')

# BestBuy Playstation Page
# browser.get("https://www.https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")

# BestBuy Purchasable Page
browser.get("https://www.bestbuy.com/site/jabra-elite-85t-true-wireless-advanced-active-noise-cancelling-earbuds-gold-beige/6450396.p?skuId=6450396")

buyButton = False

while not buyButton:

    try:
        # If this works then the button is not open
        addToCartBtn = browser.find_element_by_class_name("btn-disabled")

        # Button isn't open restart the script
        print("Button isn't ready yet.")

        # Refresh page after a delay
        time.sleep(1)
        browser.refresh()

    except:
        firstBtn = browser.find_element_by_class_name("btn-primary").click()

        # Click the button and end the script
        print("First button was clicked.")

        secondBtn = browser.find_element_by_class_name("btn-secondary").click()

        print("Second button was clicked.")

        addToCartBtn = browser.find_element_by_class_name("btn-lg").click()

        print("Add to Cart button was clicked.")

        # goToCartBtn = browser.find_element_by_class_name("btn-sm").click()

        # print("Go to Cart button was clicked.")
        buyButton = True
