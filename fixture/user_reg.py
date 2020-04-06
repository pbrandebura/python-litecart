from selenium.webdriver.support.select import Select
from time import sleep


class UserReg:
    def __init__(self, app):
        self.app = app

    def create_account(self, user):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="box-account-login"]/div/form/table/tbody/tr[5]/td/a').click()
        self.fill_contact_form(user)
        self.select_country_dropdown(user)
        driver.find_element_by_name("create_account").click()
        user_created_info = driver.find_element_by_css_selector(".notice ").text
        expected_info = " Your customer account has been created."
        assert expected_info, user_created_info

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="box-account"]/div/ul/li[4]/a').click()

    def user_login(self, user):
        driver = self.app.driver
        driver.find_element_by_name('email').send_keys(user.email)
        driver.find_element_by_name('password').send_keys(user.password)
        driver.find_element_by_name('login').click()

    def fill_contact_form(self, user):
        self.type("firstname", user.firstname)
        self.type("lastname", user.lastname)
        self.type("address1", user.address1)
        self.type("postcode", user.postcode)
        self.type("city", user.city)
        self.type("email", user.email)
        self.type("phone", user.phone)
        self.type("password", user.password)
        self.type("confirmed_password", user.password)

    def type(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def select_country_dropdown(self, user):
        driver = self.app.driver
        s1 = Select(driver.find_element_by_xpath("//*[@name='country_code']"))

        for opt in s1.options:
            s1.select_by_visible_text(user.country)
