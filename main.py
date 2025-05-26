import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot("YOUR_BOT_TOKEN")  # tokenni o'zingizning haqiqiy tokeningizga almashtiring

# Til bo‘yicha foydalanuvchi holatini saqlash
user_lang = {}

# Til tanlash menyusi
def language_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("🇺🇿 O‘zbek tili"), KeyboardButton("🇷🇺 Русский язык"))
    return markup

# O‘zbekcha menyu
def uzbek_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("ℹ️ Universitet haqida", "📚 Ta’lim yo‘nalishlari")
    markup.row("🎓 O‘quv tizimi", "💰 Grant va stipendiyalar")
    markup.row("🌐 Hamkorlik", "📍 Joylashuv")
    markup.row("📞 Aloqa")
    return markup

# Ruscha menyu
def russian_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("ℹ️ О университете", "📚 Образовательные направления")
    markup.row("🎓 Учебная система", "💰 Гранты и стипендии")
    markup.row("🌐 Сотрудничество", "📍 Локация")
    markup.row("📞 Контакты")
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🇺🇿 Tilni tanlang / 🇷🇺 Выберите язык", reply_markup=language_menu())

@bot.message_handler(func=lambda msg: msg.text in ["🇺🇿 O‘zbek tili", "🇷🇺 Русский язык"])
def set_language(message):
    chat_id = message.chat.id
    lang = "uz" if message.text == "🇺🇿 O‘zbek tili" else "ru"
    user_lang[chat_id] = lang

    welcome = "Cyber University rasmiy botiga xush kelibsiz!" if lang == "uz" else "Добро пожаловать в официальный бот Cyber University!"
    menu = uzbek_menu() if lang == "uz" else russian_menu()

    bot.send_message(chat_id, welcome, reply_markup=menu)

@bot.message_handler(func=lambda msg: True)
def reply_handler(message):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id)

    if not lang:
        bot.send_message(chat_id, "Iltimos, tilni tanlang. / Пожалуйста, выберите язык.", reply_markup=language_menu())
        return

    msg = message.text

    if lang == "uz":
        if msg == "ℹ️ Universitet haqida":
            bot.send_message(chat_id,
                "📄 *Cyber University haqida:*\n\n"
                "O‘zbekiston Respublikasi Prezidentining 2025-yil 20-yanvardagi PQ–14-sonli qarori asosida tashkil etilgan.\n"
                "[Qarorni o‘qish](https://lex.uz/uz/docs/-7332592)\n\n"
                "⚙️ Cyber University — O‘zbekistonning raqamli kelajagiga yo‘l ochuvchi zamonaviy oliy ta’lim dargohi.\n\n"
                "✅ *Bosh maqsad:* xalqaro raqobatbardosh, innovatsion fikrlaydigan va amaliy ko‘nikmaga ega kiberxavfsizlik mutaxassislarini tayyorlash.",
                parse_mode="Markdown", disable_web_page_preview=True)

        elif msg == "📚 Ta’lim yo‘nalishlari":
            bot.send_message(chat_id,
                "*📚 Bakalavriat yo‘nalishlari:*\n"
                "- Kiberxavfsizlik injiniringi: tarmoq va tizim xavfsizligi\n"
                "- Kompyuter injiniringi: sun’iy intellekt\n"
                "- Kiberxavfsizlik injiniringi: internet ashyolari xavfsizligi\n"
                "- Dasturiy injiniring: amaliy matematika va algoritmlashtirish\n"
                "- Yurisprudensiya: kiber huquq\n"
                "- Yurisprudensiya: raqamli kriminalistika\n"
                "- Menejment: kiberxavfsizlik menejmenti\n"
                "- Iqtisodiyot: raqamli iqtisodiyot\n\n"
                "*😎 Magistratura yo‘nalishlari:*\n"
                "- Axborot xavfsizligi\n"
                "- Kiber huquq", parse_mode="Markdown")

        elif msg == "🎓 O‘quv tizimi":
            bot.send_message(chat_id,
                "*🎓 O‘quv tizimi:*\n\n"
                "- 1 yil Foundation, 3 yil asosiy ta’lim\n"
                "- Ta’lim to‘liq ingliz tilida olib boriladi\n"
                "- Kredit-modul tizimi asosida o‘qitish\n"
                "- Amaliyot IT kompaniyalari va texnoparklarda tashkil etiladi", parse_mode="Markdown")

        elif msg == "💰 Grant va stipendiyalar":
            bot.send_message(chat_id,
                "*💰 Grant va stipendiyalar:*\n\n"
                "- 2025/2026 o‘quv yili uchun 100 ta davlat granti\n"
                "- Stipendiyalar sanoat hamkorlari va Innovatsion rivojlanish kengashi ko‘magida", parse_mode="Markdown")

        elif msg == "🌐 Hamkorlik":
            bot.send_message(chat_id,
                "*🌐 Xalqaro hamkorlik:*\n\n"
                "Cyber University orqali xalqaro ta’lim imkoniyatlariga ega bo‘ling:\n"
                "- AQSH, Xitoy, Yaponiya davlat universitetlari bilan 2+2 va 3+1 o‘quv dasturlari", parse_mode="Markdown")

        elif msg == "📍 Joylashuv":
            bot.send_message(chat_id,
                "📍 *Manzil:* Toshkent viloyati, Nurafshon shahri\n"
                "[Xaritada ko‘rish](https://maps.app.goo.gl/tsgXZ2x8QUos6dSV7)",
                parse_mode="Markdown")

        elif msg == "📞 Aloqa":
            bot.send_message(chat_id,
                "*📞 Aloqa uchun:* \n"
                "☎️ +998 (55) 888-55-55\n"
                "📱 +998 (95) 182-71-17", parse_mode="Markdown")

        else:
            bot.send_message(chat_id, "Iltimos, menyudan birini tanlang.", reply_markup=uzbek_menu())

    elif lang == "ru":
        if msg == "ℹ️ О университете":
            bot.send_message(chat_id,
                "📄 *О Cyber University:*\n\n"
                "Основан по постановлению Президента Республики Узбекистан PQ–14 от 20 января 2025 года.\n"
                "[Читать постановление](https://lex.uz/uz/docs/-7332592)\n\n"
                "⚙️ Cyber University — современное высшее учебное заведение, открывающее путь к цифровому будущему Узбекистана.\n\n"
                "✅ *Цель:* Подготовка конкурентоспособных, инновационно мыслящих специалистов в области кибербезопасности.",
                parse_mode="Markdown", disable_web_page_preview=True)

        elif msg == "📚 Образовательные направления":
            bot.send_message(chat_id,
                "*📚 Бакалавриат:*\n"
                "- Кибербезопасность: безопасность сетей и систем\n"
                "- Компьютерная инженерия: искусственный интеллект\n"
                "- Кибербезопасность: безопасность Интернета вещей\n"
                "- Программная инженерия: прикладная математика и алгоритмы\n"
                "- Юриспруденция: кибер право\n"
                "- Юриспруденция: цифровая криминалистика\n"
                "- Менеджмент: управление кибербезопасностью\n"
                "- Экономика: цифровая экономика\n\n"
                "*😎 Магистратура:*\n"
                "- Информационная безопасность\n"
                "- Кибер право", parse_mode="Markdown")

        elif msg == "🎓 Учебная система":
            bot.send_message(chat_id,
                "*🎓 Учебная система:*\n\n"
                "- 1 год Foundation, 3 года основное обучение\n"
                "- Обучение полностью на английском языке\n"
                "- Кредитно-модульная система\n"
                "- Практика в IT-компаниях и технопарках", parse_mode="Markdown")

        elif msg == "💰 Гранты и стипендии":
            bot.send_message(chat_id,
                "*💰 Гранты и стипендии:*\n\n"
                "- 100 государственных грантов на 2025/2026 учебный год\n"
                "- Стипендии от отраслевых партнеров и Совета инновационного развития", parse_mode="Markdown")

        elif msg == "🌐 Сотрудничество":
            bot.send_message(chat_id,
                "*🌐 Международное сотрудничество:*\n\n"
                "Возможности международного образования через Cyber University:\n"
                "- Программы 2+2 и 3+1 с университетами США, Китая, Японии", parse_mode="Markdown")

        elif msg == "📍 Локация":
            bot.send_message(chat_id,
                "📍 *Адрес:* Ташкентская область, город Нурафшан\n"
                "[Посмотреть на карте](https://maps.app.goo.gl/tsgXZ2x8QUos6dSV7)",
                parse_mode="Markdown")

        elif msg == "📞 Контакты":
            bot.send_message(chat_id,
                "*📞 Контакты:* \n"
                "☎️ +998 (55) 888-55-55\n"
                "📱 +998 (95) 182-71-17", parse_mode="Markdown")

        else:
            bot.send_message(chat_id, "Пожалуйста, выберите вариант из меню.", reply_markup=russian_menu())

bot.polling(non_stop=True)
