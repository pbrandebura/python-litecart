from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Basket:

    def __init__(self, app):
        self.app = app

    def add_product_from_most_popular(self):
        driver = self.app.driver
        self.add_product_to_basket("box-most-popular", '1')
        self.go_to_homepage()

    def add_product_from_campaigns(self):
        driver = self.app.driver
        self.add_product_to_basket("box-campaigns", '2')
        self.go_to_homepage()

    def add_product_from_latest_products(self):
        driver = self.app.driver
        self.add_product_to_basket("box-latest-products", '3')

    def add_product_to_basket(self, product_list, size):
        driver = self.app.driver
        product = driver.find_element_by_xpath('//*[@id="' + product_list + '"]/div/ul/li[1]').click()
        basket_qty_before_adding = driver.find_element_by_css_selector('span.quantity').text
        self.choose_item_size(size)
        add_to_cart_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "add_cart_product")))
        add_to_cart_btn.click()
        self.basket_status_check(basket_qty_before_adding)

    def basket_status_check(self, actual_basket_status):
        driver = self.app.driver
        expected_value = 1 + int(actual_basket_status)
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.quantity'), str(expected_value)))

    def choose_item_size(self, size):
        driver = self.app.driver
        try:
            driver.implicitly_wait(1)
            driver.find_element_by_css_selector('td.options')
            s1 = Select(driver.find_element_by_name('options[Size]'))
            for opt in s1.options:
                s1.select_by_index(size)
        except NoSuchElementException:
            pass

    def go_to_homepage(self):
        driver = self.app.driver
        driver.find_element_by_css_selector('#logotype-wrapper').click()

    def open_basket(self):
        driver = self.app.driver
        driver.find_element_by_css_selector('div#cart').click()

    def clear_basket(self):
        driver = self.app.driver
        expected_value = "Customer Details"
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#box-checkout-customer > h2'), expected_value))
        items_in_basket = driver.find_elements_by_css_selector('td.sku')
        for element in range(0, len(items_in_basket)+1):
            remove_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "remove_cart_item")))
            remove_button.click()
        empty_cart_info = "There are no items in your cart."
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#checkout-cart-wrapper > p:nth-child(1) > em'), empty_cart_info))
