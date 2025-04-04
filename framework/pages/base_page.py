from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url
        self._timeout = 10

    def wait_for_element(self, locator, timeout: int = None):
        """Повертає об'єкт очікування для WebDriver"""
        timeout = timeout if timeout is not None else self._timeout
        return WebDriverWait(self.driver, timeout)

    def open(self, url: str = None):
        """Відкриває сторінку за вказаним URL або URL за замовчуванням"""
        target_url = url or self.url
        if not target_url:
            raise ValueError("URL не вказано")
        self.driver.get(url=target_url)

    def find_element(self, locator, timeout: int = None):
        """Знаходить елемент за локатором з очікуванням його появи"""
        try:
            return self.wait_for_element(locator, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException as e:
            raise TimeoutException(f"Елемент не знайдено за локатором {locator}: {e}")

    def get_text(self, locator, timeout: int = None):
        """Отримує текст елемента"""
        return self.find_element(locator=locator, timeout=timeout).text

    def click(self, locator, timeout: int = None):
        """Клікає на елемент з очікуванням його клікабельності"""
        try:
            element = self.wait_for_element(locator, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except Exception as e:
            raise Exception(f"Не вдалося клікнути на елемент {locator}: {e}")

    def input_text(self, locator, text, timeout: int = None):
        """Вводить текст у елемент"""
        element = self.find_element(locator=locator, timeout=timeout)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator, timeout: int = None):
        """Перевіряє видимість елемента"""
        try:
            return self.wait_for_element(locator, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    def drag_and_drop(self, source_locator, target_locator, timeout: int = None):
        """Перетягує елемент з одного місця в інше"""
        source = self.find_element(source_locator, timeout)
        target = self.find_element(target_locator, timeout)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def hover(self, locator, timeout: int = None):
        """Наводить курсор на елемент"""
        element = self.find_element(locator, timeout)
        ActionChains(self.driver).move_to_element(element).perform()

    def switch_to_frame(self, frame_locator, timeout: int = None):
        """Переключається на фрейм"""
        frame = self.find_element(frame_locator, timeout)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        """Переключається на основний контент"""
        self.driver.switch_to.default_content()

    def accept_alert(self):
        """Приймає alert"""
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """Відхиляє alert"""
        self.driver.switch_to.alert.dismiss()

    def get_alert_text(self):
        """Отримує текст alert"""
        return self.driver.switch_to.alert.text

    def is_enabled(self, locator, timeout: int = None) -> bool:
        """Перевіряє, чи активний елемент"""
        return self.find_element(locator, timeout).is_enabled()

    def is_selected(self, locator, timeout: int = None) -> bool:
        """Перевіряє, чи вибраний елемент"""
        return self.find_element(locator, timeout).is_selected()

    def select_dropdown_option(self, locator, option_text, timeout: int = None):
        """Вибирає опцію з випадаючого списку за текстом"""
        select = Select(self.find_element(locator, timeout))
        select.select_by_visible_text(option_text)

    def get_page_title(self):
        """Отримує заголовок сторінки"""
        return self.driver.title

    def refresh_page(self):
        """Оновлює сторінку"""
        self.driver.refresh()

    def go_back(self):
        """Повертається на попередню сторінку"""
        self.driver.back()

    def go_forward(self):
        """Переходить на наступну сторінку"""
        self.driver.forward()

    def clear_cookies(self):
        """Очищує всі cookies"""
        self.driver.delete_all_cookies()

    def get_cookies(self):
        """Отримує всі cookies"""
        return self.driver.get_cookies()

    def add_cookie(self, cookie_dict: dict):
        """Додає cookie"""
        self.driver.add_cookie(cookie_dict)

    def press_key(self, locator, key: str, timeout: int = None):
        """Натискає клавішу на елементі"""
        element = self.find_element(locator, timeout)
        element.send_keys(getattr(Keys, key))

    def wait_for_text_to_be_present(self, locator, text: str, timeout: int = None):
        """Очікує появи тексту в елементі"""
        try:
            return self.wait_for_element(locator, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
        except TimeoutException:
            return False

    def wait_for_element_to_disappear(self, locator, timeout: int = None):
        """Очікує зникнення елемента"""
        try:
            return self.wait_for_element(locator, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    def execute_script(self, script: str, *args):
        """Виконує JavaScript код"""
        return self.driver.execute_script(script, *args)

    def scroll_to_element(self, locator, timeout: int = None):
        """Прокручує сторінку до елемента"""
        element = self.find_element(locator, timeout)
        self.execute_script("arguments[0].scrollIntoView(true);", element)