from framework.locators.text_box_page_locators import TextBoxLocators
from framework.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
        self.scroll_to_element(TextBoxLocators.SUBMIT_BUTTON)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TextBoxLocators.SUBMIT_BUTTON)
        )
        
        self.click(TextBoxLocators.SUBMIT_BUTTON)

    def get_name_in_output_box_text(self):
        return self.get_text(TextBoxLocators.NAME_OUTPUT_BOX)

    def get_email_in_output_box_text(self):
        return self.get_text(TextBoxLocators.EMAIL_OUTPUT_BOX)

    def get_current_address_output_box_test(self):
        return self.get_text(TextBoxLocators.CURRENT_ADDRESS_OUTPUT_BOX)

    def get_permanent_address_output_box_test(self):
        return self.get_text(TextBoxLocators.PERMANENT_ADDRESS_OUTPUT_BOX)

    def get_full_name_placeholder_text(self):
        return self.get_placeholder_text(TextBoxLocators.FULL_NAME_PLACEHOLDER)

    def get_email_placeholder_text(self):
        return self.get_placeholder_text(TextBoxLocators.EMAIL_PLACEHOLDER)

    def get_current_address_placeholder_text(self):
        return self.get_placeholder_text(TextBoxLocators.CURRENT_ADDRESS_PLACEHOLDER)

    def get_permanent_address_placeholder_text(self):
        return self.get_placeholder_text(TextBoxLocators.PERMANENT_ADDRESS_PLACEHOLDER)
