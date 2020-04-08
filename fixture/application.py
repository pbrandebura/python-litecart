from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.store_front import StoreFront
from fixture.admin_panel import AdminPanel
from fixture.user import User
from fixture.product import Product
from fixture.basket import Basket

class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.store_front = StoreFront(self)
        self.admin_panel = AdminPanel(self)
        self.user = User(self)
        self.product = Product(self)
        self.basket = Basket(self)

    def destroy(self):
        self.driver.quit()
