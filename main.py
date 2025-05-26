import telebot
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

# Til menyusi
def language_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🇺🇿 O‘zbekcha", "🇷🇺 Русский")
    return markup

# Asosiy menyu - O‘zbek
def main_menu_uz():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("ℹ️ Universitet haqida", "📚 Ta’lim yo‘nalishlari")
    markup.row("🎓 O‘quv tizimi", "💰 Grant va stipendiyalar")
    markup.row("🌐 Hamkorlik", "📍 Joylashuv")
    markup.row("📞 Aloqa")
    return markup

# Asosiy menyu - Rus
def main_menu_ru():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("ℹ️ Об университете", "📚 Образовательные направления")
    markup.row("🎓 Система обучения", "💰 Гранты и стипендии")
    markup.row("🌐 Сотрудничество", "📍 Локация")
    markup.row("📞 Контакты")
    return markup

# Tilni saqlash
user_language = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🇺🇿 Tilni tanlang / 🇷🇺 Выберите язык:", reply_markup=language_menu())

@bot.message_handler(func=lambda message: message.text in ["🇺🇿 O‘zbekcha", "🇷🇺 Русский"])
def set_language(message):
    user_language[message.chat.id] = message.text
    if message.text == "🇺🇿 O‘zbekcha":
        bot.send_message(message.chat.id, "Til: O‘zbek tili", reply_markup=main_menu_uz())
    else:
        bot.send_message(message.chat.id, "Язык: Русский", reply_markup=main_menu_ru())

@bot.message_handler(func=lambda message: True)
def reply_handler(message):
    lang = user_language.get(message.chat.id)

    if lang == "🇺🇿 O‘zbekcha":
        if message.text == "ℹ️ Universitet haqida":
            text = (
                "📄 *Cyber University haqida:*\n\n"
                "O‘zbekiston Respublikasi Prezidentining 2025-yil 20-yanvardagi PQ–14-sonli qarori asosida tashkil etilgan.\n"
                "[Qarorni o‘qish](https://lex.uz/uz/docs/-7332592)\n\n"
                "⚙️ Cyber University — zamonaviy oliy ta’lim dargohi.\n"
                "✅ *Bosh maqsad:* xalqaro raqobatbardosh kiberxavfsizlik mutaxassislarini tayyorlash."
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", disable_web_page_preview=True)

        elif message.text == "📚 Ta’lim yo‘nalishlari":
            text = (
                "*📚 Bakalavriat:*\n"
                "- Kiberxavfsizlik injiniringi\n"
                "- Kompyuter injiniringi\n"
                "- Dasturiy injiniring\n"
                "- Yurisprudensiya\n"
                "- Menejment\n"
                "- Iqtisodiyot\n\n"
                "*🎓 Magistratura:*\n"
                "- Axborot xavfsizligi\n"
                "- Kiber huquq"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown")

        elif message.text == "🎓 O‘quv tizimi":
            text = (
                "*🎓 O‘quv tizimi:*\n"
                "- 1 yil Foundation, 3 yil ta’lim\n"
                "- Ingliz tilida o‘qitish\n"
                "- Kredit-modul tizimi\n"
                "- Amaliyot IT kompaniyalarda"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown")

        elif message.text == "💰 Grant va stipendiyalar":
            text = (
                "*💰 Grantlar:*\n"
                "- 2025/2026 yili uchun 100 ta davlat granti\n"
                "- Sanoat hamkorlari stipendiyalari"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown")

        elif message.text == "🌐 Hamkorlik":
            text = (
                "*🌐 Xalqaro hamkorlik:*\n"
                "- AQSH, Xitoy, Yaponiya bilan 2+2, 3+1 dasturlar"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown")

        elif message.text == "📍 Joylashuv":
            bot.send_message(
                message.chat.id,
                "📍 *Manzil:* Toshkent viloyati, Nurafshon shahri\n"
                "[Xaritada ko‘rish](https://maps.app.goo.gl/tsgXZ2x8QUos6dSV7)",
                parse_mode="Markdown"
            )

        elif message.text == "📞 Aloqa":
            bot.send_message(
                message.chat.id,
                "*📞 Aloqa:*\n"
                "☎️ +998 (55) 888-55-55\n📱 +998 (95) 182-71-17",
                parse_mode="Markdown"
            )
        else:
            bot.send_message(message.chat.id, "Iltimos, menyudan tanlang.", reply_markup=main_menu_uz())

    elif lang == "🇷🇺 Русский":
        if message.text == "ℹ️ Об университете":
            text = (
                "📄 *О Cyber University:*\n\n"
                "Создан по решению Президента Узбекистана PQ–14 от 20 января 2025 года.\n"
                "[Читать указ](https://lex.uz/uz/docs/-7332592)\n\n"
                "⚙️ Cyber University — современный вуз для цифрового будущего.\n"
                "✅ *Цель:* подготовка специалистов в области кибербезопасности."
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", disable_web_page_preview=True)

        elif message.text == "📚 Образовательные направления":
            text = (
                "*📚 Бакалавриат:*\n"
                "- Инженерия кибербезопасности\n"
                "- Компьютерная инженерия\n"
                "- Программная инженерия\n"
                "- Юриспруденция\n"
                "- Менеджмент\n"
                "- Экономика\n\n"
                "*🎓 Магистратура:*\n"
                "- Информационная безопасность\n"
                "- Киберправо"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown")

        elif message.text == "🎓 Система обучения":
            text = (
                "*🎓 Система обучения:*\n"
                "- 1 год Foundation, 3 года обучения\n"
                "- Обучение на английском\n"
                "- Кредитно-модульная система\n"
                "- Практика в IT-компаниях"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown")

        elif message.text == "💰 Гранты и стипендии":
            text = (
                "*💰 Гранты и стипендии:*\n"
                "- 100 государственных грантов на 2025/2026 год\n"
                "- Стипендии от партнёров"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown")

        elif message.text == "🌐 Сотрудничество":
            text = (
                "*🌐 Международное сотрудничество:*\n"
                "- Программы 2+2 и 3+1 с вузами США, Китая и Японии"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown")

        elif message.text == "📍 Локация":
            bot.send_message(
                message.chat.id,
                "📍 *Адрес:* Ташкентская область, город Нурафшан\n"
                "[Посмотреть на карте](https://maps.app.goo.gl/tsgXZ2x8QUos6dSV7)",
                parse_mode="Markdown"
            )

        elif message.text == "📞 Контакты":
            bot.send_message(
                message.chat.id,
                "*📞 Контакты:*\n"
                "☎️ +998 (55) 888-55-55\n📱 +998 (95) 182-71-17",
                parse_mode="Markdown"
            )
        else:
            bot.send_message(message.chat.id, "Пожалуйста, выберите из меню.", reply_markup=main_menu_ru())

    else:
        bot.send_message(message.chat.id, "🇺🇿 Tilni tanlang / 🇷🇺 Выберите язык:", reply_markup=language_menu())

# Ishga tushirish
bot.polling(non_stop=True)
