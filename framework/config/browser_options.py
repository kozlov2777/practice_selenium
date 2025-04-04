from abc import ABC, abstractmethod

from selenium import webdriver


class BrowserOptions(ABC):
    def __init__(self, headless: bool = False):
        self.headless = headless

    @abstractmethod
    def get_options(self):
        pass


class ChromeOptions(BrowserOptions):
    def get_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        if self.headless:
            options.add_argument("--headless")

        return options


class FirefoxOption(BrowserOptions):
    def get_options(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")

        if self.headless:
            options.add_argument("--headless")

        return options


class EdgeOption(BrowserOptions):
    def get_options(self):
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")

        if self.headless:
            options.add_argument("--headless")

        return options


class BrowserFactory:
    browser_options = {
        "chrome": ChromeOptions,
        "firefox": FirefoxOption,
        "edge": EdgeOption
    }

    @classmethod
    def get_browser_options(cls, browser_name: str, headless: bool = True):
        name = browser_name.lower()

        if name not in cls.browser_options.keys():
            raise ValueError(f"Unsupported browser: {name}")

        option_class = cls.browser_options[name]
        options = option_class(headless).get_options()

        return options
