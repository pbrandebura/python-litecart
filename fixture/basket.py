from time import sleep
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
        self.add_product_to_basket("box-most-popular")
        sleep(5)
        self.basket_status_check(1)
        self.go_to_homepage()

    def add_product_from_campaigns(self):
        driver = self.app.driver
        self.add_product_to_basket("box-campaigns")
        sleep(5)
        self.basket_status_check(2)
        self.go_to_homepage()

    def add_product_from_latest_products(self):
        driver = self.app.driver
        self.add_product_to_basket("box-latest-products")
        sleep(5)
        self.basket_status_check(3)
        self.go_to_homepage()

    def basket_status_check(self, expected_value):
        driver = self.app.driver
        basket_status = driver.find_element_by_css_selector('span.quantity').text
        print("Hey to jest basket status:" + basket_status)
        assert int(basket_status) == expected_value

    def go_to_homepage(self):
        driver = self.app.driver
        driver.find_element_by_css_selector('#logotype-wrapper').click()

    def add_product_to_basket(self, product_list):
        driver = self.app.driver
        product = driver.find_element_by_xpath('//*[@id="' + product_list + '"]/div/ul/li[1]').click()
        self.choose_item_size()
        sleep(2)
        driver.find_element_by_name('add_cart_product').click()

    def choose_item_size(self):
        driver = self.app.driver

        try:
            driver.implicitly_wait(1)
            driver.find_element_by_css_selector('td.options')
            s1 = Select(driver.find_element_by_name('options[Size]'))
            for opt in s1.options:
                s1.select_by_index('1')
        except NoSuchElementException:
            pass

    def open_basket(self):
        driver = self.app.driver
        driver.find_element_by_css_selector('div#cart').click()

    def clear_basket(self):
        driver = self.app.driver
        wait = WebDriverWait(driver, 5)
        remove_button = wait.until(EC.presence_of_element_located(By.NAME("remove_cart_item")))
        remove_button.click()
