# Selenium Grid Test Framework

Автоматизоване тестування з використанням Selenium WebDriver та Selenium Grid.

## Особливості

- Підтримка паралельного запуску тестів на декількох браузерах (Chrome, Firefox, Edge)
- Запуск через Docker та Selenium Grid
- Підтримка логування та відображення інформативних повідомлень
- Параметризація тестів для повторного запуску з різними параметрами

## Передумови

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.10+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation) (опціонально, для локальної розробки)

## Структура фреймворку

```
.
├── framework/
│   ├── config/                  # Конфігурація браузерів
│   │   └── browser_options.py   # Фабрика опцій браузерів
│   ├── locators/                # Локатори елементів сторінки
│   └── pages/                   # Page Object класи для сторінок
├── test/
│   ├── fixtures/                # Pytest фікстури
│   │   ├── config_fixtures.py   # Фікстури для конфігурації драйверів
│   │   └── page_fixtures.py     # Фікстури для створення сторінок
│   └── test_*.py                # Файли з тестами
├── docker-compose.yml           # Конфігурація Docker для Grid
├── Dockerfile                   # Конфігурація Docker для тестів
├── run_tests.sh                 # Скрипт для запуску тестів
├── start_grid.sh                # Скрипт для запуску Selenium Grid
└── stop_grid.sh                 # Скрипт для зупинки Selenium Grid
```

## Швидкий старт

### Запуск Selenium Grid та тестів

```bash
# Запуск Grid та тестів на Chrome та Firefox
./start_grid.sh -b chrome,firefox

# Запуск в headless режимі
./start_grid.sh -b chrome,firefox --headless

# Запуск конкретного тесту
./start_grid.sh -b chrome,firefox -k test_title_text
```

### Зупинка Selenium Grid

```bash
./stop_grid.sh
```

## Запуск тестів на різних браузерах

Фреймворк підтримує автоматичний запуск тестів на всіх вказаних браузерах без необхідності додаткової параметризації в коді:

```bash
# Запуск всіх тестів на Chrome і Firefox
./run_tests.sh -b chrome,firefox

# Запуск всіх тестів на трьох браузерах
./run_tests.sh -b chrome,firefox,edge

# Запуск в headless режимі
./run_tests.sh -b chrome,firefox --headless

# Запуск конкретного тесту
./run_tests.sh -b chrome,firefox -k test_browser_title
```

### Як це працює

1. Командний аргумент `--browser` приймає список браузерів через кому.
2. Фікстура `driver` в `config_fixtures.py` автоматично параметризується для кожного браузера.
3. Кожен тест, який використовує фікстуру `driver`, буде запущений окремо для кожного браузера.

### Приклад результатів запуску

```
Running tests with the following settings:
Browsers: chrome,firefox
Grid URL: http://selenium-hub:4444/wd/hub
Command: python -m pytest --browser=chrome,firefox

test_example.py::test_browser_title[chrome] PASSED
test_example.py::test_browser_title[firefox] PASSED
test_example.py::test_multiple_sites[chrome-https://www.google.com-Google] PASSED
test_example.py::test_multiple_sites[chrome-https://www.python.org-Python] PASSED
test_example.py::test_multiple_sites[chrome-https://www.github.com-GitHub] PASSED
test_example.py::test_multiple_sites[firefox-https://www.google.com-Google] PASSED
test_example.py::test_multiple_sites[firefox-https://www.python.org-Python] PASSED
test_example.py::test_multiple_sites[firefox-https://www.github.com-GitHub] PASSED
```

## Написання тестів

### Приклад базового тесту

```python
def test_example(driver):
    # Відкриття сторінки
    driver.get("https://www.example.com")
    
    # Перевірка заголовка
    assert "Example" in driver.title
```

### Приклад тесту з параметризацією URL

```python
@pytest.mark.parametrize("url,expected_title", [
    ("https://www.google.com", "Google"),
    ("https://www.python.org", "Python"),
    ("https://www.github.com", "GitHub")
])
def test_multiple_sites(driver, url, expected_title):
    # Відкриваємо тестову сторінку
    driver.get(url)
    
    # Перевіряємо заголовок сторінки
    assert expected_title in driver.title
```

### Приклад з використанням Page Object

```python
def test_login(login_page):
    # Відкриття сторінки
    login_page.open()
    
    # Введення даних
    login_page.enter_username("test_user")
    login_page.enter_password("password123")
    login_page.click_login_button()
    
    # Перевірка успішного входу
    assert login_page.is_logged_in()
```

## Усунення проблем

### Проблеми з підключенням до Grid

- Перевірте статус контейнерів: `docker-compose ps`
- Перегляньте логи Hub: `docker-compose logs selenium-hub`
- Переконайтесь, що URL Grid правильний: `http://localhost:4444/wd/hub`

### Проблеми з браузерами

- Спробуйте запустити без headless режиму для налагодження
- Перегляньте логи браузерів: `docker-compose logs chrome` або `docker-compose logs firefox`

## Ліцензія

MIT 