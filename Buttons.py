from Setup import Login
from selenium.webdriver.common.by import By
import time


class Buttons(Login):
    def __init__(self):
        super(Buttons, self).__init__()

    # presses the checkbox buttons in order and resets them at the end, method practice_website
    # () needs to be called before this one
    def button_checkbox(self):
        self.wait_by_id("buttons").click()
        self.wait_by_id("checkboxes").click()
        for i in range(1, 6):
            for j in range(1, 4):
                self.find_element(By.ID, f"checkbox{j}").click()
                time.sleep(0.5)
        self.find_element(By.XPATH, "//*[@id='content']/form/div/button").click()

    # clicks the radio buttons in order, displaying a message if they are enabled or disabled, method practice_website
    # () needs to be called before this one
    def button_radio(self):
        self.wait_by_id("buttons").click()
        self.wait_by_id("radio-buttons").click()
        for i in range(1, 6):
            for j in range(1, 5):
                if self.find_element(By.ID, f"radio-button{j}").is_enabled():
                    self.find_element(By.ID, f"radio-button{j}").click()
                    time.sleep(0.5)
                    print(f"Button {j} is enabled")
                else:
                    print(f"Button {j} is disabled")
                    continue

