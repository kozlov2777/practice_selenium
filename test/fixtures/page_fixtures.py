import pytest

from framework.pages.text_box_page import TextBoxPage

@pytest.fixture
def text_box_page(driver):
    return TextBoxPage(driver, "https://demoqa.com/text-box")