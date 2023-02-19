from Setup import Login
from selenium.webdriver.common.by import By


class NewElement(Login):
    def __init__(self):
        super(NewElement, self).__init__()

    # opens a new tab and switches to it, prints a message if it worked by checking if it cna find
    # an element on the new window
    def new_tab(self):
        self.get("https://qa-practice.netlify.app/tab.html")
        self.find_element(By.ID, "newTabBtn").click()
        handles = self.window_handles[1]
        self.switch_to.window(handles)
        if self.find_element(By.XPATH, "/html/body/div/div/h2").text == "Table Example":
            print("works")
        else:
            print("maybe works")

    # opens a new browser window and switches to it, prints a message if it worked by checking if it cna find
    # an element on the new window
    def new_window(self):
        self.get("https://qa-practice.netlify.app/window.html")
        self.find_element(By.ID, "newWindowBtn").click()
        handles = self.window_handles[1]
        self.switch_to.window(handles)
        if self.find_element(By.XPATH, "//*[@id='content']/h2").text == "Table Example":
            print("works")
        else:
            print("maybe works")
