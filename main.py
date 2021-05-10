from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def check_exists(path):
    try:
        browser.find_element_by_id(path)
    except NoSuchElementException:
        return False
    return True


order_product = r"Pepperoni with tomatoes"

# Opening website on menu page
browser = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe")
browser.get(r"https://freelike76.github.io/kpi_web_3/#menu")
browser.implicitly_wait(5)

# Clicking on product
browser.find_element_by_id(order_product).click()
browser.implicitly_wait(5)

# Ordering
browser.find_element_by_id("buttonOrder").click()
browser.implicitly_wait(5)

# Going to cart page
browser.find_element_by_id("cart").click()
browser.implicitly_wait(5)

# Checking whether the product is in the cart
assert check_exists(order_product)
browser.close()
