from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test():
    url = "http://localhost/litecart/admin/"
    wd = webdriver.Firefox()
    wd.get(url)
    WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.ID, 'box-login')))
    wd.find_element(By.NAME, 'username').send_keys("admin")
    wd.find_element(By.NAME, 'password').send_keys("admin")
    wd.find_element(By.NAME, 'login').click()
    wd.quit()
