from Alerts import Alerts
from Btn_Acction import BtnAction
from Buttons import Buttons
from File_Upload import FileUpload
from Iframes import Iframe
from NewTab_Window import NewElement
from Scrape import ScrapeTables
from Sign_up import SignUpForm


if __name__ == '__main__':
    item_alert = Alerts()
    item_alert.alert_alert()
    item_alert.alert_confirmation("accept")

    item_btn_action = BtnAction()
    item_btn_action.btn_act_double_click()
    item_btn_action.btn_mouse_hover()
    item_btn_action.btn_act_scroll()

    item_buttons = Buttons()
    item_buttons.practice_website().button_checkbox()
    item_buttons.practice_website().button_radio()

    item_file_upload = FileUpload()
    item_file_upload.upload_file("path_to_file", "file_name")

    item_iframe = Iframe()
    item_iframe.iframe()

    item_new_window = NewElement()
    item_new_window.new_window()
    item_new_window.new_tab()

    item_tables = ScrapeTables()
    item_tables.table_static()

    item_sign_up = SignUpForm()
    item_sign_up.practice_website().sign_up_form_window()\
        .fill_signup_form("first_name", "last_name", 1234567899, "thisisanemanil@email.com", "passpassword")\
        .country_signup_form("Angola").terms_signup_form().registration_sign_up().confirmation_signup_form()
    pass
