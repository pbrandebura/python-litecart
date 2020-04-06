from selenium.webdriver.common.keys import Keys

from model.product import Product
from selenium.webdriver.support.select import Select
from time import sleep


class Product:
    def __init__(self, app):
        self.app = app

    def add_new_product(self, product):
        driver = self.app.driver
        self.open_add_new_product_view()
        self.add_info_general_tab(product)
        self.add_info_information_tab(product)
        sleep(5)
        self.add_info_prices_tab()
        self.save_product()
        sleep(5)
        expected_success_info = " Changes saved"
        actual_success_info = driver.find_element_by_xpath('//*[@id="notices"]/div').text
        assert actual_success_info == expected_success_info

    def open_add_new_product_view(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/a[2]/i').click()

    def save_product(self):
        driver = self.app.driver
        driver.find_element_by_name("save").click()

    def add_info_general_tab(self, product):
        driver = self.app.driver
        expected_h1_tag = ' Add New Product'
        actual_h1_tag = driver.find_element_by_xpath('//*[@id="content"]/h1/span').text
        assert expected_h1_tag, actual_h1_tag
        # set status to enabled
        driver.find_element_by_xpath('//*[@name="status" and @value="1"]').click()
        sleep(2)
        self.type("name[en]", "kaczka")
        self.type("code", "ffff")
        self.type("quantity", product.quantity)
        # set rubber ducks category
        driver.find_element_by_xpath('//*[@name="categories[]" and @value="1"] ').click()
        # select unisex Gender
        driver.find_element_by_xpath('//*[@value="1-3"]').click()
        self.set_date_from("05042020", "05042020")
        self.select_dropdown_value("sold_out_status_id", "Temporary sold out")
        driver.find_element_by_xpath('//*[@name="status" and @value="1"]').click()


    def set_date_from(self, date_from, date_to):
        driver = self.app.driver
        driver.find_element_by_name("date_valid_from").send_keys(date_from)
        driver.find_element_by_name("date_valid_to").send_keys(date_to)

    def add_info_information_tab(self, product):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="content"]/form/div/ul/li[2]/a').click()
        self.select_dropdown_value("manufacturer_id", "ACME Corp.")
        full_description = driver.find_element_by_css_selector('div.trumbowyg-editor')
        full_description.click()
        full_description.send_keys(product.full_description)
        self.type('short_description[en]', product.short_description)

    def add_info_prices_tab(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="content"]/form/div/ul/li[4]/a').click()
        self.type("purchase_price", "232")
        self.type("prices[USD]", "4555")
        # self.select_dropdown_value("purchase_price_currency_code", "USD")

    def select_dropdown_value(self, locator, value):
        driver = self.app.driver
        s1 = Select(driver.find_element_by_name(locator))

        for opt in s1.options:
            s1.select_by_visible_text(value)

    def type(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)
