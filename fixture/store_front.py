from model.product import Product


class StoreFront:

    def __init__(self, app):
        self.app = app 

    def navigate_to_litecart_shop(self):
        driver = self.app.driver
        driver.get("http://localhost/litecart/en/")

    def get_first_campaign_product_details_store_front(self):
        driver = self.app.driver
        product_name = driver.find_element_by_css_selector('#box-campaigns > div > ul > li > a.link .name').text
        # price locators
        regular_price_front = driver.find_element_by_css_selector(
            '#box-campaigns > div > ul > li > a.link > div.price-wrapper > s')
        campaign_price_front = driver.find_element_by_css_selector(
            '#box-campaigns > div > ul > li > a.link > div.price-wrapper > strong')
        # regular price details
        regular_price_value = regular_price_front.text
        regular_price_front_strikethrough = regular_price_front.value_of_css_property("text-decoration-line")

        # campagin price details
        campaign_price_value = campaign_price_front.text
        campaign_price_colour = campaign_price_front.value_of_css_property("Color")

        return Product(product_name=product_name, regular_price_value=regular_price_value,
                       campaign_price_value=campaign_price_value, campaign_price_colour=campaign_price_colour,
                       regular_price_line_through=regular_price_front_strikethrough)

    def open_pdp_for_first_product(self):
        driver = self.app.driver
        driver.find_element_by_css_selector('#box-campaigns > div > ul > li > a.link').click()

    def get_product_details_from_pdp(self):
        driver = self.app.driver
        # PDP - product details page
        product_name_pdp = driver.find_element_by_css_selector('#box-product .title').text
        # price locators
        regular_price_pdp = driver.find_element_by_css_selector('div.price-wrapper > s')
        campaign_price_pdp = driver.find_element_by_css_selector('.campaign-price')
        # regular price
        regular_price_pdp_value = regular_price_pdp.text
        regular_price_pdp_strikethrough = regular_price_pdp.value_of_css_property("text-decoration-line")
        # campaign price
        campaign_price_pdp_value = campaign_price_pdp.text
        campaign_price_pdp_colour = campaign_price_pdp.value_of_css_property("Color")

        return Product(product_name=product_name_pdp, regular_price_value=regular_price_pdp_value,
                       campaign_price_value=campaign_price_pdp_value, campaign_price_colour=campaign_price_pdp_colour,
                       regular_price_line_through=regular_price_pdp_strikethrough)

    def sale_label_qty_checker(self, list_name):
        driver = self.app.driver
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
