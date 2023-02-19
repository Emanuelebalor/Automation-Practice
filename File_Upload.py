from Setup import Login
from selenium.webdriver.common.by import By
import time


class FileUpload(Login):
    def __init__(self):
        super(FileUpload, self).__init__()

    # Uploads a file to the website
    def upload_file(self, path, filename):
        """
        Uploads a file on a website, may not work if the button is in a different frame

        :param path: Path to the file on the local machine
        :param filename: name of the file
        :return: None
        """
        self.get("https://qa-practice.netlify.app/file-upload.html")
        time.sleep(2)
        self.wait_by_id("file_upload").send_keys(path)
        time.sleep(2)
        self.find_element(By.XPATH, "/html/body/div/div/div[1]/div/button").click()
        if self.wait_by_id("file_upload_response").text == f'You have successfully uploaded "{filename}"':
            print("correct file uploaded")
        else:
            print("could not find the response")
