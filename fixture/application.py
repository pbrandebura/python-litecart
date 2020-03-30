from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.store_front import StoreFront
from fixture.admin_panel import AdminPanel


class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(60)
        self.store_front = StoreFront(self)
        self.admin_panel = AdminPanel(self)

    def destroy(self):
        self.driver.quit()
