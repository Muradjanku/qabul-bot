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
    markup.row("🌐 Xalqaro hamkorlik", "📍 Joylashuv")
    markup.row("📞 Aloqa", "↩️ Menyuga qaytish")
    return markup

# Asosiy menyu - Rus
def main_menu_ru():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("ℹ️ Об университете", "📚 Образовательные направления")
    markup.row("🎓 Система обучения", "💰 Гранты и стипендии")
    markup.row("🌐 Международное сотрудничество", "📍 Локация")
    markup.row("📞 Контакты", "↩️ Вернуться в меню")
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
                "⚙️ *O‘zbekiston Respublikasi Prezidentining 2025-yil 20-yanvardagi PQ–14-sonli qaroriga asosan, \"Cyber University\" - davlat universiteti tashkil etildi.*\n"
                "[Qarorni o‘qish](https://lex.uz/uz/docs/-7332592)\n\n"
                "✅ *Universitetning bosh maqsadi* — xalqaro raqobatbardosh, innovatsion fikrlaydigan va amaliy ko‘nikmaga ega kiberxavfsizlik mutaxassislarini tayyorlashdan iborat."
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", disable_web_page_preview=True, reply_markup=main_menu_uz())

        elif message.text == "📚 Ta’lim yo‘nalishlari":
            text = (
                "*📚 Ta’lim yo‘nalishlari:*\n\n"
                "*🎓 Bakalavriat:*\n"
                "• Kiberxavfsizlik injiniringi: Tarmoq va tizim xavfsizligi\n"
                "• Kiberxavfsizlik injiniringi: Internet ashyolari xavfsizligi\n"
                "• Kompyuter injiniringi: Sun’iy intellekt\n"
                "• Dasturiy injiniring: Amaliy matematika va algoritmlashtirish\n"
                "• Yurisprudensiya: Kiber huquq\n"
                "• Yurisprudensiya: Raqamli kriminalistika\n"
                "• Menejment: Kiberxavfsizlik menejmenti\n"
                "• Iqtisodiyot: Raqamli iqtisodiyot\n\n"
                "*🎓 Magistratura:*\n"
                "• Axborot xavfsizligi\n"
                "• Kiber huquq"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_uz())

        elif message.text == "🎓 O‘quv tizimi":
            text = (
                "*🎓 O‘quv tizimi:*\n"
                "1. Ta‘lim shakli: kunduzgi\n"
                "2. O‘quv davri: 4 yil\n"
                "3. Ta‘lim tizimi: Kredit-modul tizimi\n"
                "4. Amaliyot: IT kompaniyalarida"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_uz())

        elif message.text == "💰 Grant va stipendiyalar":
            text = (
                "*💰 Grantlar:*\n"
                "- 2025/2026 yili uchun 100 ta davlat granti\n"
                "- Sanoat hamkorlari stipendiyalari"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_uz())

        elif message.text == "🌐 Xalqaro hamkorlik":
            text = (
                "*🌐 Xalqaro hamkorlik:*\n"
                "Universitet AQSH, Xitoy va Yaponiya va boshqa xorijiy davlatlarning yetakchi universitetlari bilan hamkorlik qiladi.\n"
                "Ilg‘or ta’lim dasturlari va xorijiy mutaxassislar jalb etiladi."
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_uz())

        elif message.text == "📍 Joylashuv":
            text = (
                "*📍 Manzil:*\n"
                "Toshkent viloyati, Nurafshon shahri, Yangiobod MFY, Yangiobod k., 42-uy"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_uz())

        elif message.text == "📞 Aloqa":
            text = (
                "*📞 Aloqa:*\n"
                "☎️ Telefon: [+998 (55) 888-55-55](tel:+998558885555)\n"
                "📱 Telefon: [+998 (95) 182-71-17](tel:+998951827117)\n"
                "📘 Facebook: [Cyber University](https://www.facebook.com/share/1AUAavip98/?mibextid=wwXIfr)\n"
                "📸 Instagram: [cyberuni.uz](https://www.instagram.com/cyberuni.uz?igsh=czN4bTRub3ExMGRp)\n"
                "✈️ Telegram: [cyberuni_uz](https://t.me/cyberuni_uz)"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_uz())

        elif message.text == "↩️ Menyuga qaytish":
            bot.send_message(message.chat.id, "🇺🇿 Tilni tanlang:", reply_markup=language_menu())

        else:
            bot.send_message(message.chat.id, "Iltimos, menyudan tanlang.", reply_markup=main_menu_uz())

    elif lang == "🇷🇺 Русский":
        if message.text == "ℹ️ Об университете":
            text = (
                "⚙️ *В соответствии с указом Президента Республики Узбекистан PQ–14 от 20 января 2025 года создан государственный университет \"Cyber University\".*\n"
                "[Читать указ](https://lex.uz/uz/docs/-7332592)\n\n"
                "✅ *Основная цель университета* — подготовка конкурентоспособных на международном уровне, инновационно мыслящих и обладающих практическими навыками специалистов по кибербезопасности."
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", disable_web_page_preview=True, reply_markup=main_menu_ru())

        elif message.text == "📚 Образовательные направления":
            text = (
                "*📚 Образовательные направления:*\n\n"
                "*🎓 Бакалавриат:*\n"
                "• Инженерия кибербезопасности: Сетевая и системная безопасность\n"
                "• Инженерия кибербезопасности: Безопасность интернета вещей\n"
                "• Компьютерная инженерия: Искусственный интеллект\n"
                "• Программная инженерия: Прикладная математика и алгоритмизация\n"
                "• Юриспруденция: Киберправо\n"
                "• Юриспруденция: Цифровая криминалистика\n"
                "• Менеджмент: Менеджмент кибербезопасности\n"
                "• Экономика: Цифровая экономика\n\n"
                "*🎓 Магистратура:*\n"
                "• Информационная безопасность\n"
                "• Киберправо"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_ru())

        elif message.text == "🎓 Система обучения":
            text = (
                "*🎓 Система обучения:*\n"
                "1. Форма обучения: очная\n"
                "2. Период обучения: 4 года\n"
                "3. Система обучения: кредитно-модульная\n"
                "4. Практика: в IT-компаниях"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_ru())

        elif message.text == "💰 Гранты и стипендии":
            text = (
                "*💰 Гранты и стипендии:*\n"
                "- 100 государственных грантов на 2025/2026 год\n"
                "- Стипендии от партнёров"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_ru())

        elif message.text == "🌐 Международное сотрудничество":
            text = (
                "*🌐 Международное сотрудничество:*\n"
                "Университет сотрудничает с ведущими университетами США, Китая, Японии и других зарубежных стран.\n"
                "Привлекаются передовые образовательные программы и иностранные специалисты."
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_ru())

        elif message.text == "📍 Локация":
            text = (
                "*📍 Адрес:*\n"
                "Ташкентская область, город Нурафшан, МФЙ Янгиобод, улица Янгиобод, дом 42"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_ru())

        elif message.text == "📞 Контакты":
            text = (
                "*📞 Контакты:*\n"
                "☎️ Телефон: [+998 (55) 888-55-55](tel:+998558885555)\n"
                "📱 Телефон: [+998 (95) 182-71-17](tel:+998951827117)\n"
                "📘 Facebook: [Cyber University](https://www.facebook.com/share/1AUAavip98/?mibextid=wwXIfr)\n"
                "📸 Instagram: [cyberuni.uz](https://www.instagram.com/cyberuni.uz?igsh=czN4bTRub3ExMGRp)\n"
                "✈️ Telegram: [cyberuni_uz](https://t.me/cyberuni_uz)"
            )
            bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_ru())

        elif message.text == "↩️ Вернуться в меню":
            bot.send_message(message.chat.id, "🇷🇺 Выберите язык:", reply_markup=language_menu())

        else:
            bot.send_message(message.chat.id, "Пожалуйста, выберите из меню.", reply_markup=main_menu_ru())

    else:
        bot.send_message(message.chat.id, "🇺🇿 Tilni tanlang / 🇷🇺 Выберите язык:", reply_markup=language_menu())

# Ishga tushirish
bot.polling(non_stop=True)
