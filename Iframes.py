from Setup import Login
from selenium.webdriver.common.by import By
import time


class Iframe(Login):
    def __init__(self):
        super(Login, self).__init__()

    # switches from the main frame to another frame on the webpage
    def iframe(self):
        self.get("https://qa-practice.netlify.app/iframe.html")
        self.maximize_window()
        self.switch_to.frame("iframe-checkboxes")
        time.sleep(5)
        self.find_element(By.XPATH, "//*[@id='learn-more']").click()
        self.wait_by_id("show-text")
        if self.find_element(By.ID, "show-text").text == 'This text appears when you click the "Learn more" button':
            print("message displayed")
        else:
            print("message could not be found")
