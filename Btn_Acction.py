from Setup import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class BtnAction(Login):
    def __init__(self):
        super(BtnAction, self).__init__()

    def btn_act_double_click(self):
        self.get("https://qa-practice.netlify.app/double-click.html")
        self.wait_by_id("double-click-btn")
        ActionChains(self).double_click(self.find_element(By.ID, "double-click-btn")).perform()
        self.wait_by_id("double-click-result")
        if self.find_element(By.ID, "double-click-result").text == "Congrats, you double clicked!":
            print("double click works")
        else:
            print("double click does not work")

    def btn_act_scroll(self):
        self.get("https://qa-practice.netlify.app/scroll.html")
        time.sleep(2)
        ActionChains(self).scroll_to_element(self.find_element(By.ID, "the-end")).perform()

    def btn_mouse_hover(self):
        self.get("https://qa-practice.netlify.app/mouse-hover.html")
        time.sleep(2)
        ActionChains(self).move_to_element(self.find_element(By.ID, "demo")).perform()
        time.sleep(1)
        ActionChains(self).move_to_element(self.find_element(By.ID, "button-hover-over")).perform()
        if self.find_element(By.ID, "demo").text == "HOVERED":
            print("Hover works")
        else:
            print("Hover doesn't work")


