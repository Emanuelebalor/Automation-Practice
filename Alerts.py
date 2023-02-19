import time
from Setup import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Alerts(Login):
    def __init__(self):
        super(Alerts, self).__init__()

    # presses a button , waits 10 seconds for the alert and presses OK
    def alert_alert(self):
        self.get("https://qa-practice.netlify.app/alerts.html")
        self.wait_by_id("alert-btn").click()
        time.sleep(2)
        WebDriverWait(self, 10).until(EC.alert_is_present())
        time.sleep(2)
        self.switch_to.alert.accept()

    # action can be accept or dismiss, either presses ok on the alert or cancel
    def alert_confirmation(self, action):
        self.get("https://qa-practice.netlify.app/alerts.html")
        self.wait_by_id("confirm-btn").click()
        WebDriverWait(self, 30).until(EC.alert_is_present())
        if action == "accept":
            time.sleep(2)
            self.switch_to.alert.accept()
        elif action == "dismiss":
            time.sleep(2)
            self.switch_to.alert.dismiss()
