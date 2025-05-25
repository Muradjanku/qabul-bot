from telebot import TeleBot, types

TOKEN = "SIZNING_BOT_TOKENINGIZNI_BU_YERGA_QO'YING"
bot = TeleBot(TOKEN)

# Foydalanuvchi tilni tanlash uchun menyu
def language_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("🇺🇿 O‘zbekcha", "🇷🇺 Русский")
    return markup

# Asosiy menyu O‘zbek tilida
def main_menu_uz():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ℹ️ Universitet haqida", "📚 Ta’lim yo‘nalishlari")
    markup.add("🎓 O‘quv tizimi", "💰 Grant va stipendiyalar")
    markup.add("🌐 Hamkorlik", "📍Joylashuv")
    markup.add("📞 Aloqa")
    return markup

# Asosiy menyu Rus tilida
def main_menu_ru():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ℹ️ О университете", "📚 Направления обучения")
    markup.add("🎓 Учебная система", "💰 Гранты и стипендии")
    markup.add("🌐 Сотрудничество", "📍Расположение")
    markup.add("📞 Связь")
    return markup

user_language = {}

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, "Tilni tanlang / Выберите язык", reply_markup=language_keyboard())

@bot.message_handler(func=lambda m: m.text in ["🇺🇿 O‘zbekcha", "🇷🇺 Русский"])
def choose_language(message):
    if message.text == "🇺🇿 O‘zbekcha":
        user_language[message.chat.id] = "uz"
        bot.send_message(message.chat.id, "Cyber University qabul botiga xush kelibsiz!\nTanlang:", reply_markup=main_menu_uz())
    else:
        user_language[message.chat.id] = "ru"
        bot.send_message(message.chat.id, "Добро пожаловать в приемную комиссию Cyber University!\nВыберите:", reply_markup=main_menu_ru())

def back_button(lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if lang == "uz":
        markup.add("🔙 Orqaga")
    else:
        markup.add("🔙 Назад")
    return markup

@bot.message_handler(func=lambda m: True)
def main_handler(message):
    lang = user_language.get(message.chat.id, "uz")

    # Orqaga tugmasi uchun
    if message.text in ["🔙 Orqaga", "🔙 Назад"]:
        if lang == "uz":
            bot.send_message(message.chat.id, "Asosiy menyu:", reply_markup=main_menu_uz())
        else:
            bot.send_message(message.chat.id, "Главное меню:", reply_markup=main_menu_ru())
        return

    if lang == "uz":
        if message.text == "ℹ️ Universitet haqida":
            text = (
                "⚙️ Cyber University — O‘zbekistonning raqamli kelajagiga yo‘l ochuvchi zamonaviy oliy ta’lim dargohi.\n\n"
                "O‘zbekiston Respublikasi Prezidentining 2025-yil 20-yanvardagi PQ–14-sonli qaroriga asosan — Cyber University tashkil etildi.\n\n"
                "Qarorni o‘qing! 🫵 https://lex.uz/uz/docs/-7332592\n\n"
                "🫥 Asosiy maqsad:\n"
                "Cyber University xalqaro raqobatbardosh, innovatsion fikrlovchi va amaliy ko‘nikmaga ega Kiberxavfsizlik mutaxassislarini tayyorlashga yo‘naltirilgan."
            )
            bot.send_message(message.chat.id, text, reply_markup=back_button(lang))
        elif message.text == "📚 Ta’lim yo‘nalishlari":
            text = (
                "📚 *Bakalavriat yo‘nalishlari:*\n"
                "- Kiberxavfsizlik injiniringi: tizimlarni himoya qilish, xavfsizlik strategiyalari.\n"
                "- Kompyuter injiniringi: apparat va dasturiy ta'minotni yaratish.\n"
                "- Dasturiy injiniring: dastur ishlab chiqish va testlash.\n"
                "- Yurisprudensiya: kiber huquq va qonunchilik asoslari.\n"
                "- Menejment: tashkilotlarni boshqarish.\n"
                "- Iqtisodiyot: iqtisodiy tahlil va boshqaruv.\n\n"
                "*Magistratura yo‘nalishlari:*\n"
                "- Axborot xavfsizligi: ilg‘or xavfsizlik tizimlari.\n"
                "- Kiber huquq: kiber jinoyatlar va qonunlar."
            )
            bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=back_button(lang))
        elif message.text == "🎓 O‘quv tizimi":
            bot.send_message(message.chat.id,
                "🎓 *O‘quv jarayoni xususiyatlari:*\n"
                "- 1 yil Foundation, 3 yil asosiy ta’lim\n"
                "- Ta’lim to‘liq ingliz tilida\n"
                "- Kredit-modul tizimi\n"
                "- Amaliyot IT kompaniyalari va texnoparklarda",
                parse_mode='Markdown', reply_markup=back_button(lang))
        elif message.text == "💰 Grant va stipendiyalar":
            bot.send_message(message.chat.id,
                "💰 *Imkoniyatlar:*\n"
                "- 2025/2026 o‘quv yili uchun 100 ta davlat granti\n"
                "- Stipendiyalar: sanoat hamkorlari va Innovatsion rivojlanish kengashi orqali",
                parse_mode='Markdown', reply_markup=back_button(lang))
        elif message.text == "🌐 Hamkorlik":
            bot.send_message(message.chat.id,
                "🌐 *Xalqaro hamkorlik:*\n"
                "- AQSH, Xitoy, Yaponiya kabi davlatlar bilan\n"
                "- Ilg‘or ta’lim dasturlari\n"
                "- Xorijiy mutaxassislar jalb etiladi",
                parse_mode='Markdown', reply_markup=back_button(lang))
        elif message.text == "📍Joylashuv":
            bot.send_message(message.chat.id, "📍 Universitet: Toshkent viloyati, Nurafshon shahri.", reply_markup=back_button(lang))
        elif message.text == "📞 Aloqa":
            bot.send_message(message.chat.id, "📞 Aloqa uchun:\n+998 (55) 888-55-55\n+998 95 182 71 17", reply_markup=back_button(lang))
        else:
            bot.send_message(message.chat.id, "Noto‘g‘ri buyruq. /start yoki tilni tanlang.", reply_markup=language_keyboard())

    else:  # Rus tili
        if message.text == "ℹ️ О университете":
            text = (
                "⚙️ Cyber University — современное высшее учебное заведение, открывающее путь в цифровое будущее Узбекистана.\n\n"
                "Создан на основании распоряжения Президента Республики Узбекистан № PQ–14 от 20 января 2025 года.\n\n"
                "Читайте распоряжение! 🫵 https://lex.uz/uz/docs/-7332592\n\n"
                "🫥 Основная цель:\n"
                "Подготовка международно конкурентоспособных, инновационно мыслящих и практико-ориентированных специалистов в области кибербезопасности."
            )
            bot.send_message(message.chat.id, text, reply_markup=back_button(lang))
        elif message.text == "📚 Направления обучения":
            text = (
                "📚 *Бакалавриат:*\n"
                "- Инженерия кибербезопасности: защита систем и стратегия безопасности.\n"
                "- Компьютерная инженерия: создание аппаратного и программного обеспечения.\n"
                "- Программная инженерия: разработка и тестирование ПО.\n"
                "- Юриспруденция: основы киберзаконов.\n"
                "- Менеджмент: управление организациями.\n"
                "- Экономика: экономический анализ и управление.\n\n"
                "*Магистратура:*\n"
                "- Информационная безопасность: продвинутые системы безопасности.\n"
                "- Киберправо: киберпреступления и законодательство."
            )
            bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=back_button(lang))
        elif message.text == "🎓 Учебная система":
            bot.send_message(message.chat.id,
                "🎓 *
