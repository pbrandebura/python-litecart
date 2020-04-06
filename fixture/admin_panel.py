class AdminPanel:
    def __init__(self, app):
        self.app = app

    def switch_off_catpcha(self):
        driver = self.app.driver
        self.login_to_admin_panel("admin", "admin")
        self.navigate_to_security_tab()
        self.set_captcha_to_false()

    def set_captcha_to_false(self):
        driver = self.app.driver
        # open edit view
        driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[7]/td[3]/a/i').click()
        # click False radiobutton
        driver.find_element_by_xpath('//*[@value="0"]').click()
        # save changes
        driver.find_element_by_xpath('//*[@name="save"]').click()
        success_info = driver.find_element_by_xpath('//*[@id="notices"]/div/i').text
        print(success_info)
        expected_message = " Changes saved"
        assert expected_message, success_info

    def navigate_to_security_tab(self):
        driver = self.app.driver
        # driver.find_element_by_xpath('//ul/li[12]/a').click()
        driver.get('http://localhost/litecart/admin/?app=settings&doc=store_info')
        driver.find_element_by_xpath("//*[@id='doc-security']").click()

    def check_if_timezones_in_alfabetical_order(self, country_code):
        driver = self.app.driver
        list_of_states = []
        for country in range(0, len(country_code)):
            driver.get('http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=' + str(
                country_code[country]))
            list_of_states_elements = driver.find_elements_by_css_selector('.dataTable tr')
            for state in range(2, len(list_of_states_elements)):
                state_name = driver.find_element_by_css_selector(
                    '#table-zones > tbody > tr:nth-child(' + str(state) + ') > td:nth-child(3) > input').get_attribute(
                    'value')
                list_of_states.append(state_name)
            assert list_of_states, sorted(list_of_states)
            list_of_states.clear()

    def get_countries_with_more_time_zones(self):
        driver = self.app.driver
        list_of_countries = driver.find_elements_by_xpath("//*[@class='row']")
        country_with_more_tz = []
        for element in range(2, len(list_of_countries) + 2):
            time_zones = driver.find_element_by_xpath(
                '//*[@id="content"]/form/table/tbody/tr[' + str(element) + ']/td[6]').text
            if int(time_zones) != 0:
                country_code = driver.find_element_by_xpath(
                    '//*[@id="content"]/form/table/tbody/tr[' + str(element) + ']/td[4]').text
                country_with_more_tz.append(country_code)
        return country_with_more_tz

    def get_country_list(self):
        driver = self.app.driver
        list_of_countries = driver.find_elements_by_xpath("//*[@class='row']")
        downloaded_list = []
        for country in range(2, len(list_of_countries) + 2):
            text_country = driver.find_element_by_xpath(
                '/html/body/div/div/div/table/tbody/tr/td[3]/form/table/tbody/tr[' + str(country) + ']/td[5]/a').text
            downloaded_list.append(text_country)
        return downloaded_list

    def navigate_to_countries_tab(self):
        driver = self.app.driver
        driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')

    def click_on_every_menu_tab(self):
        driver = self.app.driver
        menu_tabs = driver.find_elements_by_xpath("//ul//li")
        for element in range(1, len(menu_tabs)):
            driver.find_element_by_xpath("//ul/li[" + str(element) + "]").click()
            nested_menu = driver.find_elements_by_xpath("//ul[@class='docs']/li")
            for nested_element in range(1, len(nested_menu)):
                driver.find_element_by_xpath("//ul[@class='docs']//li[" + str(nested_element + 1) + "]").click()
            # TO CHECK LINE BELOW
            if element == 17:
                break

    def login_to_admin_panel(self, username, password):
        driver = self.app.driver
        driver.get('http://localhost/litecart/admin')
        driver.find_element_by_xpath("//*[@name='username']").send_keys(username)
        driver.find_element_by_xpath("//*[@name='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@name='login']").click()
        assert driver.find_element_by_css_selector('#notices > div.notice.success')

    def navigate_to_catalog_tab(self):
        driver = self.app.driver
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
        # driver.find_element_by_xpath("/html/body/div/div/div/table/tbody/tr/td[1]/div[3]/ul/li[2]/a").click()
