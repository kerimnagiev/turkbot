
# 📚 Turkish Vocabulary Bot

Этот бот для Telegram помогает изучать турецкие слова по категориям с помощью тестов с вариантами ответов.

## 🚀 Что умеет бот

- Позволяет выбрать одну из 7 категорий слов: **Фрукты**, **Овощи**, **Животные**, **Еда**, **Дом**, **Природа**, **Профессии**.
- Предлагает выбрать количество слов для изучения: 5, 10, 15 или все слова из категории.
- Проводит тестирование: показывает турецкое слово и варианты перевода на русском.
- Дает обратную связь на каждый ответ ("Верно" или "Неверно").
- Автоматически переходит к следующему вопросу.
- Завершает тест и предлагает выбрать новую категорию.

## 🛠 Технологии

- Python 3
- Библиотека `pyTelegramBotAPI` (aka `telebot`)

## 📦 Как запустить

1. Установи зависимости:
   ```bash
   pip install pyTelegramBotAPI
   ```

2. Замени токен бота:
   В файле `new turk bot.py` найди строку:
   ```python
   TOKEN = "YOUR_BOT_TOKEN"
   ```
   и вставь свой реальный токен.

3. Запусти бота:
   ```bash
   python new\ turk\ bot.py
   ```

4. Добавь бота в Telegram и начни с команды `/start`.

## 📚 Структура кода

- **Категории слов** (`word_categories`) — турецкие слова и их русские переводы.
- **Сессии пользователей** (`user_sessions`) — хранение состояния теста каждого пользователя.
- **Клавиатуры** — используются inline-кнопки для выбора категорий, количества слов и ответов на тест.
- **Обработчики**:
  - `/start` и `/categories` — начало сессии.
  - `callback_query_handler` — обработка всех кнопок.
- **Тестирование**:
  - Выбор случайных слов и перемешивание вариантов ответов.
  - Проверка ответов пользователя.
