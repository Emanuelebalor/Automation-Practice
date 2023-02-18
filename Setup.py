import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Login(webdriver.Chrome):
    # Initial set-up for the loging page
    def __init__(self, driver=r"/home/balor/Documents/Pyp/EVERYTHING_ELSE/Chrome_Drive"):
        self.driver = driver
        os.environ['PATH'] += self.driver
        super(Login, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def practice_website(self):
        self.get("https://qa-practice.netlify.app/")
        return self

    def wait_by_id(self, id_of_element: str):
        return WebDriverWait(self, 30).until(
            EC.presence_of_element_located((By.ID, f"{id_of_element}")))

    def wait_by_xpath(self, xpath_of_element: str):
        return WebDriverWait(self, 30).until(
            EC.presence_of_element_located((By.ID, f"{xpath_of_element}")))
    pass
