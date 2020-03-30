import pytest
from selenium import webdriver
from time import sleep


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Safari()
    yield
    driver.quit()


# def test_browse_through_admin_menu(test_setup):
#     login_to_admin_panel('admin', 'admin')
#     click_on_every_menu_tab()


# def test_verify_number_of_sale_label(test_setup):
#     # test to verify if no more than 1 sale label per product is displayed
#     navigate_to_litecart_shop()
#     sale_label_qty_checker("box-most-popular")
#     sale_label_qty_checker("box-campaigns")
#     sale_label_qty_checker("box-latest-products")
#
#
# def test_countries_in_alfabetical_order(test_setup):
#     login_to_admin_panel('admin', 'admin')
#     navigate_to_countries_tab()
#     list_of_country = get_country_list()
#     assert list_of_country, sorted(list_of_country)
#
#
# def test_time_zones_in_alfabetical_order(test_setup):
#     login_to_admin_panel('admin', 'admin')
#     navigate_to_countries_tab()
#     countries = get_countries_with_more_time_zones()
#     check_if_timezones_in_alfabetical_order(countries)
#
def test_confirm_pdp_opens_with_correct_details(test_setup):
    navigate_to_litecart_shop()
    select_first_product_in_campaigns()

# def test_check_EU_countries():
#     pass


def select_first_product_in_campaigns():
    product_name_front = driver.find_element_by_css_selector('#box-campaigns > div > ul > li > a.link .name').text
    regular_price_front = driver.find_element_by_css_selector('#box-campaigns > div > ul > li > a.link > div.price-wrapper > s').text
    campaign_price_front = driver.find_element_by_css_selector('#box-campaigns > div > ul > li > a.link > div.price-wrapper > strong').text
    driver.find_element_by_css_selector('#box-campaigns > div > ul > li > a.link').click()
    # PDP - product details page
    product_name_pdp = driver.find_element_by_css_selector('#box-product .title').text
    regular_price_pdp = driver.find_element_by_css_selector('div.price-wrapper > s').text
    campaign_price_pdp = driver.find_element_by_css_selector('.campaign-price').text
    assert product_name_front, product_name_pdp
    assert regular_price_front, regular_price_pdp
    assert campaign_price_front, campaign_price_pdp


def check_if_timezones_in_alfabetical_order(country_code):
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


def get_countries_with_more_time_zones():
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


def get_country_list():
    list_of_countries = driver.find_elements_by_xpath("//*[@class='row']")
    downloaded_list = []
    for country in range(2, len(list_of_countries) + 2):
        text_country = driver.find_element_by_xpath(
            '/html/body/div/div/div/table/tbody/tr/td[3]/form/table/tbody/tr[' + str(country) + ']/td[5]/a').text
        downloaded_list.append(text_country)
    return downloaded_list


def navigate_to_countries_tab():
    driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')


def navigate_to_litecart_shop():
    driver.get("http://localhost/litecart/en/")


def sale_label_qty_checker(list_name):
    products_list = driver.find_elements_by_xpath('//*[@id=' + list_name + ']/div/ul/li')
    for element in range(1, (len(products_list))):
        sale_sticker = driver.find_elements_by_css_selector(
            '#' + list_name + ' > div > ul > li:nth-child(' + str(element) + ') > a.link > div.image-wrapper > div')
        if len(sale_sticker) > 1:
            print("A product with more than one Sale label founded!")
            break
        elif len(sale_sticker) == 1:
            continue
        elif len(sale_sticker) < 1:
            continue
    print(list_name + " checked.")


def click_on_every_menu_tab():
    menu_tabs = driver.find_elements_by_xpath("//ul//li")
    sleep(2)
    for element in range(1, len(menu_tabs)):
        driver.find_element_by_xpath("//ul/li[" + str(element) + "]").click()
        sleep(0)
        nested_menu = driver.find_elements_by_xpath("//ul[@class='docs']/li")
        for nested_element in range(1, len(nested_menu)):
            driver.find_element_by_xpath("//ul[@class='docs']//li[" + str(nested_element + 1) + "]").click()
            sleep(0)
        #TO CHECK LINE BELOW
        if element == 17:
            break


def login_to_admin_panel(username, password):
    driver.get('http://localhost/litecart/admin')
    driver.find_element_by_xpath("//*[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//*[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//*[@name='login']").click()
    assert driver.find_element_by_css_selector('#notices > div.notice.success')
