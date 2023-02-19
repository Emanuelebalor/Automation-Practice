from Setup import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SignUpForm(Login):
    def __init__(self):
        super(SignUpForm, self).__init__()

    def sign_up_form_window(self):
        try:
            self.wait_by_id("forms").click()
            self.wait_by_id("register").click()
        except TimeoutError:
            self.quit()
        return self

    def fill_signup_form(self, first_name: str, last_name: str, phone: int, email: str, password: str):
        """
        Send the information to the request form

        :param first_name: User's first name
        :param last_name: User's last name
        :param phone: User's phone_number
        :param email: User's email
        :param password: User's password
        :return: self
        """
        try:
            self.wait_by_id("registerForm")

            # first name
            first_name_input = self.find_element(By.ID, "firstName")
            first_name_input.clear()
            first_name_input.send_keys(first_name)

            # last name
            last_name_input = self.find_element(By.ID, "lastName")
            last_name_input.clear()
            last_name_input.send_keys(last_name)

            # phone
            phone_input = self.find_element(By.ID, "phone")
            phone_input.clear()
            phone_input.send_keys(phone)

            # email
            phone_input = self.find_element(By.ID, "emailAddress")
            phone_input.clear()
            phone_input.send_keys(email)

            # password
            phone_input = self.find_element(By.ID, "password")
            phone_input.clear()
            phone_input.send_keys(password)

        except TimeoutError:
            self.quit()
        return self

    def country_signup_form(self, country: str):
        """
         Selects the country in the dropdown, country must exist in the dropdown

         :param country: (str) Country
         :return: self
         """
        select_country = self.find_element(By.ID, "countries_dropdown_menu")
        choice = Select(select_country)
        choice.select_by_visible_text(country.capitalize())
        return self

    def terms_signup_form(self):
        self.find_element(By.ID, "exampleCheck1").click()
        return self

    def registration_sign_up(self):
        self.find_element(By.ID, "registerBtn").click()
        return self

    def confirmation_signup_form(self):
        try:
            self.wait_by_id("message")
            if self.find_element(By.ID, "message").text == "The account has been successfully created!":
                print("The account has been successfully created!")
        except TimeoutError:
            self.quit()

