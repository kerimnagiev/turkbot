# -*- coding: utf-8 -*-
import telebot
from telebot import types  # Импортируем типы для кнопок
import random
import time

# ВАЖНО: Замените 'YOUR_BOT_TOKEN' на ваш реальный токен бота
TOKEN = "TOKEN"
bot = telebot.TeleBot(TOKEN)

# Словарь категорий с 15 словами в каждой
# ВНИМАНИЕ: Приведены примеры слов. Замените их на реальные турецко-русские пары.
word_categories = {
    "Фрукты": {
        "elma": "яблоко", "muz": "банан", "çilek": "клубника", "portakal": "апельсин",
        "armut": "груша", "kiraz": "вишня", "üzüm": "виноград", "karpuz": "арбуз",
        "kavun": "дыня", "şeftali": "персик", "kayısı": "абрикос", "nar": "гранат",
        "incir": "инжир", "limon": "лимон", "mandalina": "мандарин",
        "ananas": "ананас", "avokado": "авокадо", "mango": "манго", "papaya": "папайя",
        "kiwi": "киви", "hurma": "финик", "kivi": "киви", "böğürtlen": "ежевика",
        "ahududu": "малина", "yaban mersini": "черника", "kızılcık": "клюква",
        "dut": "шелковица", "kestane": "каштан", "ceviz": "грецкий орех"
    },
    "Овощи": {
        "patates": "картофель", "havuç": "морковь", "soğan": "лук", "salatalık": "огурец",
        "domates": "помидор", "biber": "перец", "patlıcan": "баклажан", "kabak": "кабачок",
        "ıspanak": "шпинат", "brokoli": "брокколи", "lahana": "капуста", "mantar": "гриб",
        "bezelye": "горох", "fasulye": "фасоль", "sarımsak": "чеснок",
        "marul": "салат", "turp": "редис", "pırasa": "лук-порей", "kereviz": "сельдерей",
        "enginar": "артишок", "bamya": "бамия", "karnabahar": "цветная капуста",
        "brüksel lahanası": "брюссельская капуста", "pancar": "свекла", "şalgam": "репа",
        "tere": "кресс-салат", "roka": "руккола", "semizotu": "портулак",
        "maydanoz": "петрушка", "dereotu": "укроп", "nane": "мята"
    },
    "Животные": {
        "kedi": "кошка", "köpek": "собака", "kuş": "птица", "balık": "рыба",
        "at": "лошадь", "inek": "корова", "koyun": "овца", "tavuk": "курица",
        "ördek": "утка", "ayı": "медведь", "kurt": "волк", "tilki": "лиса",
        "aslan": "лев", "kaplan": "тигр", "fil": "слон",
        "zebra": "зебра", "zürafa": "жираф", "maymun": "обезьяна", "panda": "панда",
        "kanguru": "кенгуру", "koala": "коала", "penguen": "пингвин", "deve": "верблюд",
        "tavşan": "кролик", "sincap": "белка", "kirpi": "ёж", "gelincik": "ласка",
        "sırtlan": "гиена", "leopar": "леопард", "geyik": "олень", "gergedan": "носорог"
    },
    "Еда": {
        "ekmek": "хлеб", "peynir": "сыр", "yumurta": "яйцо", "süt": "молоко",
        "et": "мясо", "tavuk": "курица (еда)", "balık": "рыба (еда)", "pirinç": "рис",
        "makarna": "макароны", "çorba": "суп", "salata": "салат", "tatlı": "десерт",
        "kahve": "кофе", "çay": "чай", "su": "вода",
        "yoğurt": "йогурт", "krem peynir": "творожный сыр", "tereyağı": "сливочное масло",
        "zeytinyağı": "оливковое масло", "bal": "мёд", "reçel": "варенье",
        "dondurma": "мороженое", "kek": "торт", "börek": "пирог", "simit": "бублик",
        "pide": "лепёшка", "pilav": "плов", "köfte": "котлета", "kebap": "кебаб",
        "pizza": "пицца", "hamburger": "гамбургер", "sandviç": "сэндвич"
    },
    "Дом": {
        "ev": "дом", "oda": "комната", "kapı": "дверь", "pencere": "окно",
        "masa": "стол", "sandalye": "стул", "yatak": "кровать", "dolap": "шкаф",
        "mutfak": "кухня", "banyo": "ванная", "tuvalet": "туалет", "lamba": "лампа",
        "halı": "ковер", "perde": "штора", "anahtar": "ключ",
        "koltuk": "диван", "kanepe": "кресло", "sehpa": "журнальный столик",
        "kitaplık": "книжный шкаф", "ayna": "зеркало", "çerçeve": "рамка",
        "vazo": "ваза", "saat": "часы", "telefon": "телефон", "televizyon": "телевизор",
        "buzdolabı": "холодильник", "fırın": "духовка", "çamaşır makinesi": "стиральная машина",
        "bulaşık makinesi": "посудомоечная машина", "süpürge": "пылесос", "ütü": "утюг"
    },
    "Природа": {
        "ağaç": "дерево", "çiçek": "цветок", "nehir": "река", "göl": "озеро",
        "deniz": "море", "dağ": "гора", "orman": "лес", "güneş": "солнце",
        "ay": "луна", "yıldız": "звезда", "bulut": "облако", "yağmur": "дождь",
        "kar": "снег", "rüzgar": "ветер", "taş": "камень",
        "kum": "песок", "toprak": "земля", "çimen": "трава", "yaprak": "лист",
        "dal": "ветка", "kök": "корень", "çalı": "куст", "ot": "трава",
        "yosun": "мох", "mantar": "гриб", "kaya": "скала", "vadi": "долина",
        "tepe": "холм", "ada": "остров", "yarımada": "полуостров", "körfez": "залив"
    },
    "Профессии": {
        "öğretmen": "учитель", "doktor": "врач", "mühendis": "инженер", "avukat": "адвокат",
        "polis": "полицейский", "itfaiyeci": "пожарный", "aşçı": "повар", "garson": "официант",
        "şoför": "водитель", "pilot": "пилот", "hemşire": "медсестра", "çiftçi": "фермер",
        "sanatçı": "художник", "müzisyen": "музыкант", "yazar": "писатель",
        "mimar": "архитектор", "ressam": "художник", "fotoğrafçı": "фотограф",
        "gazeteci": "журналист", "sporcu": "спортсмен", "terzi": "портной",
        "berber": "парикмахер", "kuaför": "стилист", "tamirci": "ремонтник",
        "elektrikçi": "электрик", "tamirci": "механик", "muhasebeci": "бухгалтер",
        "bankacı": "банкир", "satıcı": "продавец", "kasiyer": "кассир", "güvenlik görevlisi": "охранник"
    }
}

# Хранилище для текущего теста пользователя
user_sessions = {}

# --- Функции для создания клавиатур ---


def create_category_keyboard():
    """Создает клавиатуру с кнопками для выбора категорий."""
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    for category_name in word_categories.keys():
        button = types.InlineKeyboardButton(
            text=category_name, callback_data=f"cat_{category_name}")
        buttons.append(button)
    markup.add(*buttons)
    return markup


def create_number_choice_keyboard(category_name):
    """Создает клавиатуру для выбора количества слов."""
    markup = types.InlineKeyboardMarkup(row_width=2)
    total_words_in_category = len(word_categories[category_name])
    options = [5, 10, 15]  # Стандартные опции
    buttons = []

    # Добавляем кнопки для стандартных опций, если они меньше или равны общему числу слов
    for num in options:
        if num <= total_words_in_category:
            buttons.append(types.InlineKeyboardButton(
                text=str(num), callback_data=f"num_{category_name}_{num}"))

    # Добавляем кнопку "Все слова", если стандартных опций меньше, чем всего слов,
    # или если последняя стандартная опция не равна общему числу слов
    if not options or options[-1] < total_words_in_category:
        buttons.append(types.InlineKeyboardButton(
            text=f"Все ({total_words_in_category})", callback_data=f"num_{category_name}_all"))

    markup.add(*buttons)
    return markup


def create_start_test_keyboard():
    """Создает клавиатуру с кнопкой для начала теста."""
    markup = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(
        text="✅ Начать тест", callback_data="cmd_start_test")
    markup.add(button)
    return markup

# --- Обработчики команд ---


@bot.message_handler(commands=['start', 'categories'])
def send_category_choice(message):
    """Обработчик команд /start и /categories. Отправляет сообщение с выбором категорий."""
    chat_id = message.chat.id
    # Удаляем предыдущую сессию
    if chat_id in user_sessions:
        previous_message_id = user_sessions[chat_id].get("message_id")
        if previous_message_id:
            try:
                bot.delete_message(chat_id, previous_message_id)
            except Exception as e:
                print(
                    f"Не удалось удалить старое сообщение {previous_message_id}: {e}")
        del user_sessions[chat_id]

    markup = create_category_keyboard()
    bot.send_message(
        chat_id, "Привет! 👋 Выбери категорию слов для изучения:", reply_markup=markup)

# --- Логика теста ---


def prompt_number_of_words(chat_id, category_name, message_id_to_edit=None):
    """Спрашивает у пользователя, сколько слов он хочет выучить."""
    print(f"Запрос количества слов для {chat_id}, категория: {category_name}")
    # Редактируем сообщение выбора категории, убирая кнопки
    if message_id_to_edit:
        try:
            bot.edit_message_text(f"Выбрана категория: *{category_name}*", chat_id, message_id_to_edit,
                                  reply_markup=None, parse_mode="Markdown")
        except Exception as e:
            print(
                f"Не удалось отредактировать сообщение {message_id_to_edit}: {e}")

    markup = create_number_choice_keyboard(category_name)
    bot.send_message(
        chat_id, f"Сколько слов из категории '{category_name}' ты хочешь выучить?", reply_markup=markup)


def setup_session_and_prompt_start(chat_id, category_name, num_words_choice, message_id_to_edit=None):
    """Настраивает сессию с выбранным количеством слов и предлагает начать тест."""
    print(
        f"Настройка сессии для {chat_id}, категория: {category_name}, количество: {num_words_choice}")
    all_words_in_category = list(word_categories[category_name].items())
    random.shuffle(all_words_in_category)  # Перемешиваем весь список категории

    words_for_session = []
    if num_words_choice == "all":
        words_for_session = all_words_in_category
    else:
        try:
            num = int(num_words_choice)
            # Берем срез, но не больше, чем есть слов в категории
            words_for_session = all_words_in_category[:min(
                num, len(all_words_in_category))]
        except ValueError:
            print(
                f"Ошибка преобразования количества слов: {num_words_choice}. Используем все слова.")
            words_for_session = all_words_in_category  # По умолчанию берем все, если ошибка

    actual_num_words = len(words_for_session)
    if actual_num_words == 0:
        print(
            f"Ошибка: Не удалось выбрать слова для сессии {chat_id}, категория {category_name}")
        bot.send_message(
            chat_id, "Произошла ошибка при выборе слов. Попробуйте выбрать категорию заново.")
        return

    # Удаляем старую сессию перед созданием новой
    if chat_id in user_sessions:
        del user_sessions[chat_id]

    # Создаем сессию с выбранным количеством слов
    user_sessions[chat_id] = {
        "category": category_name,
        "words": words_for_session,  # Используем подготовленный список
        "current_word": None,
        "options": [],
        "message_id": None
    }
    print(
        f"Сессия создана для {chat_id}, категория: {category_name}, слов: {actual_num_words}")

    # Редактируем сообщение выбора количества слов
    if message_id_to_edit:
        try:
            bot.edit_message_text(f"Категория: *{category_name}*. Количество слов: *{actual_num_words}*",
                                  chat_id, message_id_to_edit, reply_markup=None, parse_mode="Markdown")
        except Exception as e:
            print(
                f"Не удалось отредактировать сообщение {message_id_to_edit}: {e}")

    markup = create_start_test_keyboard()
    bot.send_message(
        chat_id, f"Отлично! Готов(а) начать тест ({actual_num_words} слов)?", reply_markup=markup)


def initiate_test(chat_id, message_id_to_edit=None):
    """Начинает тест: задает первый вопрос (слова уже перемешаны при создании сессии)."""
    session = user_sessions.get(chat_id)

    if session and session["words"]:
        if message_id_to_edit:
            try:
                bot.edit_message_text(
                    f"Поехали! 🚀 ({len(session['words'])} слов)", chat_id, message_id_to_edit, reply_markup=None)
            except Exception as e:
                print(
                    f"Не удалось отредактировать сообщение {message_id_to_edit}: {e}")

        print(f"Начинаем тест для {chat_id}. Слова: {len(session['words'])}")
        # Слова уже перемешаны и отобраны на шаге setup_session_and_prompt_start
        ask_question(chat_id)
    elif session and not session["words"]:
        bot.send_message(
            chat_id, "Ты уже прошел(ла) тест по этой категории или не было выбрано слов. Выбери другую (/categories).")
    else:
        bot.send_message(
            chat_id, "Сначала выбери категорию и количество слов (/categories).")


def ask_question(chat_id):
    """Задает вопрос пользователю, предлагая варианты ответа в виде кнопок."""
    session = user_sessions.get(chat_id)

    if not session:
        print(f"Сессия для {chat_id} не найдена в ask_question.")
        return

    if not session["words"]:
        # Сообщение о завершении теста
        # Получаем общее число слов в исходной категории
        total_learned = len(word_categories.get(
            session.get("category", ""), {}))
        bot.send_message(
            chat_id, f"Поздравляю! 🎉 Тест по категории '{session.get('category', 'выбранной')}' завершен!")
        if chat_id in user_sessions:
            del user_sessions[chat_id]
        bot.send_message(
            chat_id, "Выбери новую категорию для изучения (/categories).")
        return

    word, correct_translation = session["words"][0]
    session["current_word"] = (word, correct_translation)
    current_category = session["category"]
    print(f"Задаем вопрос для {chat_id} ({current_category}): {word}?")

    # Выбираем неверные варианты ТОЛЬКО из текущей категории
    current_category_words = word_categories[current_category]
    category_translations = list(current_category_words.values())
    possible_wrong_options = list(
        set(category_translations) - {correct_translation})

    num_wrong_options = min(3, len(possible_wrong_options))
    options = random.sample(possible_wrong_options, num_wrong_options)
    options.append(correct_translation)

    while len(options) < 4:
        options.append(f"Неверный вариант {len(options)+1}")

    random.shuffle(options)
    session["options"] = options

    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    for i, option in enumerate(options):
        button = types.InlineKeyboardButton(
            text=option, callback_data=f"ans_{i}")
        buttons.append(button)
    markup.add(*buttons)

    # Определяем номер текущего вопроса
    total_words_in_session = len(user_sessions[chat_id].get("words", [])) + (len(
        word_categories[current_category]) - len(session.get("words", [])))  # Приблизительно
    current_question_num = (
        len(word_categories[current_category]) - len(session["words"])) + 1
    total_questions = len(user_sessions[chat_id].get(
        "initial_words", session["words"]))  # Нужна доработка для точного подсчета

    # TODO: Для точного подсчета номера вопроса нужно хранить изначальное количество слов в сессии
    text = f"❓ Вопрос {current_question_num} / ?\n({current_category}) Как переводится слово \"{word}\"?"
    try:
        sent_message = bot.send_message(chat_id, text, reply_markup=markup)
        session["message_id"] = sent_message.message_id
    except Exception as e:
        print(f"Ошибка отправки сообщения в ask_question для {chat_id}: {e}")
        bot.send_message(
            chat_id, "Не удалось отправить вопрос. Попробуй /start.")
        if chat_id in user_sessions:
            del user_sessions[chat_id]

# --- Единый обработчик нажатий на ВСЕ кнопки ---


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    """Обрабатывает нажатия на все inline-кнопки."""
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    callback_data = call.data
    session = user_sessions.get(chat_id)

    print(f"Получен callback от {chat_id}: {callback_data}")

    try:
        # --- Обработка выбора категории ---
        if callback_data.startswith("cat_"):
            category_name = callback_data[4:]
            if category_name in word_categories:
                bot.answer_callback_query(
                    call.id, text=f"Выбрана категория: {category_name}")
                # Теперь не создаем сессию сразу, а спрашиваем количество слов
                prompt_number_of_words(
                    chat_id, category_name, message_id_to_edit=message_id)
            else:
                bot.answer_callback_query(
                    call.id, text="Ошибка: Категория не найдена")

        # --- Обработка выбора количества слов ---
        elif callback_data.startswith("num_"):
            parts = callback_data.split('_')  # num_{category}_{number/all}
            if len(parts) == 3:
                category_name = parts[1]
                num_choice = parts[2]  # Может быть числом или "all"
                if category_name in word_categories:
                    bot.answer_callback_query(
                        call.id, text=f"Выбрано слов: {num_choice}")
                    # Создаем сессию с нужным количеством слов и предлагаем начать тест
                    setup_session_and_prompt_start(
                        chat_id, category_name, num_choice, message_id_to_edit=message_id)
                else:
                    bot.answer_callback_query(
                        call.id, text="Ошибка: Категория не найдена")
            else:
                bot.answer_callback_query(
                    call.id, text="Ошибка в данных callback")
                print(
                    f"Некорректный callback_data для выбора числа слов: {callback_data}")

        # --- Обработка команды (старт теста) ---
        elif callback_data.startswith("cmd_"):
            command = callback_data[4:]
            if command == "start_test":
                if chat_id in user_sessions:
                    bot.answer_callback_query(call.id, text="Начинаем тест!")
                    initiate_test(chat_id, message_id_to_edit=message_id)
                else:
                    bot.answer_callback_query(
                        call.id, text="Сначала выберите категорию и количество слов.")
                    bot.send_message(
                        chat_id, "Пожалуйста, выберите категорию сначала.", reply_markup=create_category_keyboard())
                    try:
                        bot.edit_message_reply_markup(
                            chat_id, message_id, reply_markup=None)
                    except Exception as e:
                        print(
                            f"Не удалось убрать кнопку 'Начать тест' у сообщения {message_id}: {e}")
            else:
                bot.answer_callback_query(call.id, text="Неизвестная команда")

        # --- Обработка ответа на вопрос ---
        elif callback_data.startswith("ans_"):
            if not session or not session.get("current_word") or message_id != session.get("message_id"):
                bot.answer_callback_query(
                    call.id, text="Этот вопрос уже неактуален.")
                try:
                    bot.edit_message_reply_markup(
                        chat_id=chat_id, message_id=message_id, reply_markup=None)
                except Exception as e:
                    print(
                        f"Не удалось убрать кнопки у старого сообщения {message_id}: {e}")
                return

            choice_index = int(callback_data[4:])
            word, correct_translation = session["current_word"]
            current_category = session["category"]

            if 0 <= choice_index < len(session["options"]):
                chosen_translation = session["options"][choice_index]
            else:
                bot.answer_callback_query(
                    call.id, text="Ошибка варианта ответа.")
                print(
                    f"Ошибка: Неверный choice_index {choice_index} для опций {session['options']}")
                return

            try:
                bot.edit_message_text(
                    chat_id=chat_id, message_id=message_id,
                    text=f"❓ ({current_category}) Слово: \"{word}\"\nВаш ответ: {chosen_translation}",
                    reply_markup=None
                )
            except Exception as e:
                print(f"Ошибка редактирования сообщения {message_id}: {e}")

            result_message = ""
            if chosen_translation == correct_translation:
                result_message = f"✅ Верно! \"{word}\" - это \"{correct_translation}\"."
                bot.answer_callback_query(call.id, text="Правильно!")
            else:
                result_message = f"❌ Неверно. Правильный ответ: \"{correct_translation}\"."
                bot.answer_callback_query(call.id, text="Неправильно!")

            bot.send_message(chat_id, result_message)

            if session["words"]:
                session["words"].pop(0)  # Удаляем слово после ответа

            session["current_word"] = None
            session["options"] = []
            session["message_id"] = None

            time.sleep(0.7)
            ask_question(chat_id)  # Задаем следующий вопрос

        # --- Неизвестный callback ---
        else:
            bot.answer_callback_query(call.id, text="Неизвестный тип callback")
            print(f"Неизвестный callback_data: {callback_data}")

    except (ValueError, IndexError) as e:
        print(
            f"Ошибка обработки callback (ValueError/IndexError) для {chat_id}: {e}")
        bot.answer_callback_query(call.id, text="Ошибка обработки ответа.")
    except Exception as e:
        print(
            f"Непредвиденная ошибка в callback_query_handler для {chat_id}: {e}")
        bot.answer_callback_query(call.id, text="Произошла ошибка.")


# --- Запуск бота ---
if __name__ == '__main__':
    print("Бот запускается...")
    while True:
        try:
            print("Подключение к Telegram API...")
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except ConnectionError as e:
            print(
                f"Ошибка соединения: {e}. Повторная попытка через 15 секунд...")
            time.sleep(15)
        except Exception as e:
            print(f"Критическая ошибка polling: {e}")
            print("Перезапуск через 30 секунд...")
            time.sleep(30)
