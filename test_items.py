from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def tests_for_store(browser):
    browser.get(link)
    try:
        isCartFinded = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket').is_displayed()
    except NoSuchElementException:
        isCartFinded = False

    assert isCartFinded == True, "Element 'Cart' isn't finded"
    time.sleep(5)