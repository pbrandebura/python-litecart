from selenium import webdriver


def test():
    url = "http://www.google.com/"
    wd = webdriver.Firefox()
    wd.get(url)
    wd.implicitly_wait(5)
    wd.quit()