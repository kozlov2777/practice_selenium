from framework.locators.text_box_page_locators import TextBoxLocators
from framework.pages.base_page import BasePage


class TextBoxPage(BasePage):
    def get_title_text(self):
        return self.get_text(TextBoxLocators.TITLE)

    def get_full_name_label_text(self):
        return self.get_text(TextBoxLocators.FULL_NAME_LABEL)

    def fill_full_name_input(self, text: str):
        self.input_text(TextBoxLocators.FULL_NAME_INPUT, text)

    def get_email_label_text(self):
        return self.get_text(TextBoxLocators.EMAIL_LABEL)

    def fill_email_label_text(self, text: str):
        self.input_text(TextBoxLocators.EMAIL_INPUT, text)

    def get_current_address_label(self):
        return self.get_text(TextBoxLocators.CURRENT_ADDRESS_LABEL)

    def fill_current_address_input(self, text: str):
        self.input_text(TextBoxLocators.CURRENT_ADDRESS_INPUT, text)

    def get_permanent_address_label(self):
        return self.get_text(TextBoxLocators.PERMANENT_ADDRESS_LABEL)

    def fill_permanent_address_input(self, text: str):
        self.input_text(TextBoxLocators.PERMANENT_ADDRESS_INPUT, text)

    def click_submit_button(self):
        self.click(TextBoxLocators.SUBMIT_BUTTON)
