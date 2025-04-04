from selenium.webdriver.common.by import By


class TextBoxLocators:
    TITLE = (By.XPATH, '//h1[@class="text-center"]')
    FULL_NAME_LABEL = (By.XPATH, '//*[@id="userName-label"]')
    FULL_NAME_INPUT = (By.XPATH, '//input[@id="userName"]')
    EMAIL_LABEL = (By.XPATH, '//*[@id="userEmail-label"]')
    EMAIL_INPUT = (By.XPATH, '//*[@id="userEmail"]')
    CURRENT_ADDRESS_LABEL = (By.XPATH, '//*[@id="currentAddress-label"]')
    CURRENT_ADDRESS_INPUT = (By.XPATH, '//*[@id="currentAddress"]')
    PERMANENT_ADDRESS_LABEL = (By.XPATH, '//*[@id="permanentAddress-label"]')
    PERMANENT_ADDRESS_INPUT = (By.XPATH, '//*[@id="permanentAddress"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submit"]')
    NAME_OUTPUT_BOX = (By.XPATH, '//p[@id="name"]')
    EMAIL_OUTPUT_BOX = (By.XPATH, '//p[@id="email"]')
    CURRENT_ADDRESS_OUTPUT_BOX = (By.XPATH, '//p[@id="currentAddress"]')
    PERMANENT_ADDRESS_OUTPUT_BOX = (By.XPATH, '//p[@id="permanentAddress"]')
    FULL_NAME_PLACEHOLDER = (By.XPATH, '//*[@id="userName"]')
    EMAIL_PLACEHOLDER = (By.XPATH, '//*[@id="userEmail"]')
    CURRENT_ADDRESS_PLACEHOLDER = (By.XPATH, '//*[@id="currentAddress"]')
    PERMANENT_ADDRESS_PLACEHOLDER = (By.XPATH, '//*[@id="permanentAddress"]')
