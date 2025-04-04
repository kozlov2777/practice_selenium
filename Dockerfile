# Використовуємо Python як базовий образ
FROM python:3.11-slim

# Налаштування змінних середовища
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Встановлення базових утиліт
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Встановлення Poetry
RUN pip install poetry==1.8.3

# Встановлення робочої директорії
WORKDIR /app

# Копіювання poetry файлів
COPY pyproject.toml poetry.lock* ./

# Налаштування Poetry для встановлення в систему (не у віртуальне середовище)
RUN poetry config virtualenvs.create false

# Встановлення залежностей
RUN poetry install --no-interaction --no-root

# Копіювання скрипту запуску тестів
COPY run_tests.sh ./
RUN chmod +x run_tests.sh

# Копіювання всього проекту
COPY . .

# Встановлення проекту
RUN poetry install --no-interaction

# Команда за замовчуванням - запуск тестів через скрипт
CMD ["/bin/bash", "-c", "chmod +x /app/run_tests.sh && /app/run_tests.sh -b 'chrome,firefox'"]