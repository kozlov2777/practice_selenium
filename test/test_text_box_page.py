def test_title_text(text_box_page):
    """Перевірка заголовка на сторінці Text Box"""
    # Відкриваємо сторінку
    text_box_page.open()
    
    # Отримуємо текст заголовка
    title_text = text_box_page.get_title_text()
    
    # Перевіряємо, що заголовок відповідає очікуваному
    assert title_text == "Text Box", f"Очікувалось 'Text Box', але отримано: {title_text}"
    
    # Виводимо інформацію про успішно пройдений тест
    print(f"Тест на заголовок успішно пройдено. Заголовок: {title_text}")