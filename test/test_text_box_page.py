import pytest
from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts


@pytest.mark.parametrize(
    "get_method, expected_text", [
        pytest.param(
            lambda page: page.get_title_text(),
            "Text Box",
            id="Test title text on text_box page"
        ),
        pytest.param(
            lambda page: page.get_full_name_label_text(),
            "Full Name",
            id="full_name_label"
        ),
        pytest.param(
            lambda page: page.get_email_label_text(),
            "Email",
            id="email_label"
        ),
        pytest.param(
            lambda page: page.get_current_address_label(),
            "Current Address",
            id="current_address_label"
        ),
        pytest.param(
            lambda page: page.get_permanent_address_label(),
            "Permanent Address",
            id="permanent_address_label"
        ),
    ]
)
def test_text_box_page_labels(text_box_page, get_method, expected_text):
    s_assert = SoftAsserts()
    text_box_page.open()

    actual_text = get_method(text_box_page)

    s_assert.assert_equal(actual_text, expected_text, f"Очікувалось '{expected_text}', але отримано: '{actual_text}'")
    s_assert.assert_all()


@pytest.mark.parametrize(
    "input_data", [
        pytest.param(
            {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "current_address": "123 Main St, Kyiv",
                "permanent_address": "456 Oak Ave, Lviv"
            },
            id="valid_user_data"
        ),
    ]
)
def test_text_box_form_inputs_and_output(text_box_page, input_data: dict):
    s_assert = SoftAsserts()
    text_box_page.open()

    text_box_page.fill_full_name_input(input_data["name"])
    text_box_page.fill_email_label_text(input_data["email"])
    text_box_page.fill_current_address_input(input_data["current_address"])
    text_box_page.fill_permanent_address_input(input_data["permanent_address"])

    text_box_page.click_submit_button()

    name_in_output_box = text_box_page.get_name_in_output_box_text()
    email_in_output_box = text_box_page.get_email_in_output_box_text()
    current_address_in_output_box = text_box_page.get_current_address_output_box_test()
    permanent_address_in_output_box = text_box_page.get_permanent_address_output_box_test()

    s_assert.assert_equal(name_in_output_box, f'Name: {input_data["name"]}',
                      f"Неправильне ім'я у вихідному блоці. Очікувалось 'Name: {input_data['name']}', отримано '{name_in_output_box}'")
    s_assert.assert_equal(email_in_output_box, f'Email: {input_data["email"]}',
                      f"Неправильний email у вихідному блоці. Очікувалось 'Email: {input_data['email']}', отримано '{email_in_output_box}'")
    s_assert.assert_equal(current_address_in_output_box, f'Current Address: {input_data["current_address"]}',
                      f"Неправильна поточна адреса у вихідному блоці. Очікувалось 'Current Address: {input_data['current_address']}', отримано '{current_address_in_output_box}'")
    s_assert.assert_equal(permanent_address_in_output_box, f'Permanent Address: {input_data["permanent_address"]}',
                      f"Неправильна постійна адреса у вихідному блоці. Очікувалось 'Permanent Address: {input_data['permanent_address']}', отримано '{permanent_address_in_output_box}'")

    s_assert.assert_all()


@pytest.mark.parametrize(
    "expected_data",
    [
        pytest.param(
            {
                "full_name": "Full Name",
                "email": "name@example.com",
                "current_address": "Current Address",
                "permanent_address": "Permanent Address",
            },
            id="placeholder_texts"
        )
    ]
)
def test_placeholder_text_box_page(text_box_page, expected_data: dict):
    s_assert = SoftAsserts()
    text_box_page.open()

    full_name_placeholder = text_box_page.get_full_name_placeholder_text()
    email_placeholder = text_box_page.get_email_placeholder_text()
    current_address_placeholder = text_box_page.get_current_address_placeholder_text()
    permanent_address_placeholder = text_box_page.get_permanent_address_placeholder_text()

    s_assert.assert_equal(full_name_placeholder, expected_data["full_name"], "Плейсхолдер Full Name некоректний")
    s_assert.assert_equal(email_placeholder, expected_data["email"], "Плейсхолдер Email некоректний")
    s_assert.assert_equal(current_address_placeholder, expected_data["current_address"], "Плейсхолдер Current Address некоректний")
    s_assert.assert_equal(permanent_address_placeholder, expected_data["permanent_address"], "Плейсхолдер Permanent Address некоректний")

    s_assert.assert_all()


@pytest.mark.parametrize(
    "invalid_input_data", [
        pytest.param(
            {
                "name": "",
                "email": "john.doe@example.com",
                "current_address": "123 Main St, Kyiv",
                "permanent_address": "456 Oak Ave, Lviv",
                "expected_output": False
            },
            id="empty_name"
        ),
        pytest.param(
            {
                "name": "John Doe",
                "email": "",
                "current_address": "123 Main St, Kyiv",
                "permanent_address": "456 Oak Ave, Lviv",
                "expected_output": False
            },
            id="empty_email"
        ),
        pytest.param(
            {
                "name": "John Doe",
                "email": "invalid-email",
                "current_address": "123 Main St, Kyiv",
                "permanent_address": "456 Oak Ave, Lviv",
                "expected_output": False
            },
            id="invalid_email_format"
        ),
        pytest.param(
            {
                "name": "   ",
                "email": "john.doe@example.com",
                "current_address": "123 Main St, Kyiv",
                "permanent_address": "456 Oak Ave, Lviv",
                "expected_output": False
            },
            id="whitespace_only_name"
        ),
        pytest.param(
            {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "current_address": "",
                "permanent_address": "",
                "expected_output": True
            },
            id="empty_addresses"
        ),
        pytest.param(
            {
                "name": "a" * 100,
                "email": "john.doe@example.com",
                "current_address": "123 Main St, Kyiv",
                "permanent_address": "456 Oak Ave, Lviv",
                "expected_output": True
            },
            id="very_long_name"
        ),
        pytest.param(
            {
                "name": "<script>alert('XSS')</script>",
                "email": "john.doe@example.com",
                "current_address": "123 Main St, Kyiv",
                "permanent_address": "456 Oak Ave, Lviv",
                "expected_output": True
            },
            id="xss_attempt_in_name"
        ),
        pytest.param(
            {
                "name": "John Doe",
                "email": "john.doe+test123@example.co.uk",
                "current_address": "123 Main St, Kyiv",
                "permanent_address": "456 Oak Ave, Lviv",
                "expected_output": True
            },
            id="complex_valid_email"
        ),
    ]
)
def test_text_box_form_invalid_inputs(text_box_page, invalid_input_data:dict):
    """
    Тест перевіряє поведінку форми з невалідними даними.
    Деякі випадки можуть не мати явної візуальної валідації,
    тому перевіряється факт наявності або відсутності блоку виводу.
    """
    s_assert = SoftAsserts()
    text_box_page.open()

    # Заповнення форми
    text_box_page.fill_full_name_input(invalid_input_data["name"])
    text_box_page.fill_email_label_text(invalid_input_data["email"])
    text_box_page.fill_current_address_input(invalid_input_data["current_address"])
    text_box_page.fill_permanent_address_input(invalid_input_data["permanent_address"])

    # Відправка форми
    text_box_page.click_submit_button()

    # Перевірка результату в залежності від очікування
    if invalid_input_data["expected_output"]:
        # Якщо очікуємо, що дані будуть виведені
        name_in_output_box = text_box_page.get_name_in_output_box_text()
        s_assert.assert_true(bool(name_in_output_box), "Вихідний блок мав відобразитись, але його не видно")

        # Перевіряємо вміст виведених даних для полів, які були заповнені
        if invalid_input_data["name"]:
            s_assert.assert_true(invalid_input_data["name"] in name_in_output_box,
                       f"Очікувалось, що '{invalid_input_data['name']}' буде у '{name_in_output_box}'")

    else:
        # Можемо перевіряти відсутність виводу або наявність повідомлень про помилки
        # Це залежить від поведінки програми - в даному випадку припускаємо, що
        # при невалідних даних блок виводу не з'явиться або буде порожнім

        # Варіант 1: перевірка відсутності або порожності блоку виводу
        try:
            # Спроба отримати текст із блоку виводу
            output_text = text_box_page.get_name_in_output_box_text()
            # Якщо блок існує, але порожній - це також валідний результат для невалідних даних
            s_assert.assert_false(bool(output_text), "Вихідний блок не має відображатись для невалідних даних")
        except:
            # Якщо блок відсутній взагалі - це також очікуваний результат
            pass

    s_assert.assert_all()


def test_complete_form_validation(text_box_page):
    """
    Комплексний тест для перевірки заповнення форми та результатів.
    Використовує м'які перевірки (soft assert_equals) для того,
    щоб продовжити тестування навіть якщо деякі перевірки не пройдуть.
    """
    s_assert = SoftAsserts()
    test_data = {
        "name": "Oleksandr Test",
        "email": "test@example.com",
        "current_address": "Kyiv, Ukraine",
        "permanent_address": "Lviv, Ukraine"
    }

    text_box_page.open()

    # Перевірка заголовка та лейблів
    s_assert.assert_equal(text_box_page.get_title_text(), "Text Box", "Заголовок сторінки некоректний")
    s_assert.assert_equal(text_box_page.get_full_name_label_text(), "Full Name", "Лейбл Full Name некоректний")
    s_assert.assert_equal(text_box_page.get_email_label_text(), "Email", "Лейбл Email некоректний")
    s_assert.assert_equal(text_box_page.get_current_address_label(), "Current Address", "Лейбл Current Address некоректний")
    s_assert.assert_equal(text_box_page.get_permanent_address_label(), "Permanent Address", "Лейбл Permanent Address некоректний")

    # Перевірка плейсхолдерів
    s_assert.assert_equal(text_box_page.get_full_name_placeholder_text(), "Full Name", "Плейсхолдер Full Name некоректний")
    s_assert.assert_equal(text_box_page.get_email_placeholder_text(), "name@example.com", "Плейсхолдер Email некоректний")
    s_assert.assert_equal(text_box_page.get_current_address_placeholder_text(), "Current Address", "Плейсхолдер Current Address некоректний")
    s_assert.assert_equal(text_box_page.get_permanent_address_placeholder_text(), "Permanent Address", "Плейсхолдер Permanent Address некоректний")

    # Заповнення форми
    text_box_page.fill_full_name_input(test_data["name"])
    text_box_page.fill_email_label_text(test_data["email"])
    text_box_page.fill_current_address_input(test_data["current_address"])
    text_box_page.fill_permanent_address_input(test_data["permanent_address"])

    # Відправка форми
    text_box_page.click_submit_button()

    # Перевірка результатів
    s_assert.assert_equal(text_box_page.get_name_in_output_box_text(), f"Name: {test_data['name']}",
               "Неправильне ім'я у вихідному блоці")
    s_assert.assert_equal(text_box_page.get_email_in_output_box_text(), f"Email: {test_data['email']}",
               "Неправильний email у вихідному блоці")
    s_assert.assert_equal(text_box_page.get_current_address_output_box_test(), f"Current Address: {test_data['current_address']}",
               "Неправильна поточна адреса у вихідному блоці")
    s_assert.assert_equal(text_box_page.get_permanent_address_output_box_test(), f"Permanent Address: {test_data['permanent_address']}",
               "Неправильна постійна адреса у вихідному блоці")

    s_assert.assert_all()
