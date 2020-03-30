class StoreFront:

    def __init__(self, app):
        self.app = app

    def navigate_to_litecart_shop(self):
        driver = self.app.driver
        driver.get("http://localhost/litecart/en/")

    def select_first_product_in_campaigns(self):
        driver = self.app.driver
        product_name_front = driver.find_element_by_css_selector('#box-campaigns > div > ul > li > a.link .name').text
        regular_price_front = driver.find_element_by_css_selector(
            '#box-campaigns > div > ul > li > a.link > div.price-wrapper > s').text
        campaign_price_front = driver.find_element_by_css_selector(
            '#box-campaigns > div > ul > li > a.link > div.price-wrapper > strong').text
        driver.find_element_by_css_selector('#box-campaigns > div > ul > li > a.link').click()
        # PDP - product details page
        product_name_pdp = driver.find_element_by_css_selector('#box-product .title').text
        regular_price_pdp = driver.find_element_by_css_selector('div.price-wrapper > s').text
        campaign_price_pdp = driver.find_element_by_css_selector('.campaign-price').text
        assert product_name_front, product_name_pdp
        assert regular_price_front, regular_price_pdp
        assert campaign_price_front, campaign_price_pdp

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
