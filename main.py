from telebot import TeleBot, types
import os

bot = TeleBot(os.getenv("TELEGRAM_TOKEN"))  # TOKEN ni muhit o'zgaruvchisidan oling

# Boshlang'ich menyu - til tanlash
def language_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("🇺🇿 O‘zbekcha", "🇷🇺 Русский")
    bot.send_message(chat_id, "Tilni tanlang / Выберите язык:", reply_markup=markup)

# Asosiy menyu O'zbekcha
def main_menu_uz(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ℹ️ Universitet haqida", "📚 Ta’lim yo‘nalishlari")
    markup.add("🎓 O‘quv tizimi", "💰 Grant va stipendiyalar")
    markup.add("🌐 Hamkorlik", "📞 Aloqa")
    markup.add("🔙 Orqaga")
    bot.send_message(chat_id, "Cyber University qabul botiga xush kelibsiz!\nTanlang:", reply_markup=markup)

# Asosiy menyu Ruscha
def main_menu_ru(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ℹ️ О университете", "📚 Направления обучения")
    markup.add("🎓 Учебный процесс", "💰 Гранты и стипендии")
    markup.add("🌐 Сотрудничество", "📞 Связь")
    markup.add("🔙 Назад")
    bot.send_message(chat_id, "Добро пожаловать в приёмный бот Cyber University!\nВыберите:", reply_markup=markup)

@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    language_menu(message.chat.id)

@bot.message_handler(func=lambda m: m.text in ["🇺🇿 O‘zbekcha", "🇷🇺 Русский"])
def language_choice(message):
    if message.text == "🇺🇿 O‘zbekcha":
        main_menu_uz(message.chat.id)
        bot.set_state(message.from_user.id, "uzbek", None)
    else:
        main_menu_ru(message.chat.id)
        bot.set_state(message.from_user.id, "russian", None)

@bot.message_handler(func=lambda message: True)
def main_handler(message):
    user_state = bot.get_state(message.from_user.id)

    if user_state == "uzbek":
        uzbek_sections(message)
    elif user_state == "russian":
        russian_sections(message)
    else:
        # Agar til tanlanmagan bo‘lsa, yana til tanlashga yubor
        language_menu(message.chat.id)

def uzbek_sections(message):
    text = message.text

    if text == "ℹ️ Universitet haqida":
        bot.send_message(message.chat.id,
            "⚙️ Cyber University — O‘zbekistonning raqamli kelajagiga yo‘l ochuvchi zamonaviy oliy ta’lim dargohi.\n\n"
            "O‘zbekiston Respublikasi Prezidentining 2025-yil 20-yanvardagi PQ–14-sonli qaroriga asosan — Cyber University tashkil etildi.\n\n"
            "Qarorni oqing! 🫵https://lex.uz/uz/docs/-7332592\n\n"
            "🫥 Asosiy maqsad:\n"
            "Cyber University xalqaro raqobatbardosh, innovatsion fikrlovchi va amaliy ko‘nikmaga ega Kiberxavfsizlik mutaxassislarini tayyorlashga yo‘naltirilgan.",
            parse_mode='Markdown'
        )
    elif text == "📚 Ta’lim yo‘nalishlari":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Kiberxavfsizlik injiniringi")
        markup.add("Kompyuter injiniringi")
        markup.add("Dasturiy injiniring")
        markup.add("Yurisprudensiya")
        markup.add("Menejment")
        markup.add("Iqtisodiyot")
        markup.add("Magistratura yo‘nalishlari")
        markup.add("🔙 Orqaga")
        bot.send_message(message.chat.id, "Ta’lim yo‘nalishlarini tanlang:", reply_markup=markup)

    elif text == "Kiberxavfsizlik injiniringi":
        bot.send_message(message.chat.id,
            "Kiberxavfsizlik injiniringi bo‘yicha ta’lim:\n"
            "- Tarmoq xavfsizligi\n"
            "- Axborot tizimlarini himoyalash\n"
            "- Kiber hujumlarni aniqlash va oldini olish\n"
            "- Kriptografiya va shifrlash texnologiyalari\n"
            "- Amaliy laboratoriya ishlari",
            parse_mode='Markdown'
        )

    elif text == "Kompyuter injiniringi":
        bot.send_message(message.chat.id,
            "Kompyuter injiniringi bo‘yicha ta’lim:\n"
            "- Kompyuter arxitekturasi\n"
            "- Elektronika asoslari\n"
            "- Mikrokontrollerlar\n"
            "- Tizim dasturlash\n"
            "- Amaliy loyihalar",
            parse_mode='Markdown'
        )

    elif text == "Dasturiy injiniring":
        bot.send_message(message.chat.id,
            "Dasturiy injiniring bo‘yicha ta’lim:\n"
            "- Dasturiy ta’minot yaratish\n"
            "- Loyihalash va dasturlash metodologiyalari\n"
            "- Testlash va sifat nazorati\n"
            "- Jamoaviy dasturlash\n"
            "- Zamonaviy dasturlash tillari",
            parse_mode='Markdown'
        )

    elif text == "Yurisprudensiya":
        bot.send_message(message.chat.id,
            "Yurisprudensiya yo‘nalishi:\n"
            "- Huquqshunoslik asoslari\n"
            "- Kiber huquq\n"
            "- Huquqiy himoya va qonunlar\n"
            "- Amaliy mashg‘ulotlar",
            parse_mode='Markdown'
        )

    elif text == "Menejment":
        bot.send_message(message.chat.id,
            "Menejment yo‘nalishi:\n"
            "- Biznes boshqaruvi\n"
            "- Loyihalar boshqaruvi\n"
            "- Marketing asoslari\n"
            "- Rahbarlik ko‘nikmalari",
            parse_mode='Markdown'
        )

    elif text == "Iqtisodiyot":
        bot.send_message(message.chat.id,
            "Iqtisodiyot yo‘nalishi:\n"
            "- Makro va mikroiqtisodiyot\n"
            "- Moliyaviy tahlil\n"
            "- Iqtisodiy siyosat\n"
            "- Statistika va iqtisodiy modelleme",
            parse_mode='Markdown'
        )

    elif text == "Magistratura yo‘nalishlari":
        bot.send_message(message.chat.id,
            "Magistratura yo‘nalishlari:\n"
            "- Axborot xavfsizligi\n"
            "- Kiber huquq yo‘nalishlari\n\n"
            "Axborot xavfsizligi – tizimlar va ma'lumotlarni himoya qilishga qaratilgan soha.\n"
            "Kiber huquq – axborot texnologiyalari va internetda qonunlarni o‘rganadi.",
            parse_mode='Markdown'
        )

    elif text == "🎓 O‘quv tizimi":
        bot.send_message(message.chat.id,
            "🎓 O‘quv jarayoni xususiyatlari:\n"
            "- 1 yil Foundation, 3 yil asosiy ta’lim\n"
            "- Ta’lim to‘liq ingliz tilida\n"
            "- Kredit-modul tizimi\n"
            "- Amaliyot IT kompaniyalari va texnoparklarda",
            parse_mode='Markdown'
        )

    elif text == "💰 Grant va stipendiyalar":
        bot.send_message(message.chat.id,
            "💰 Imkoniyatlar:\n"
            "- 2025/2026 o‘quv yili uchun 100 ta davlat granti\n"
            "- Stipendiyalar: sanoat hamkorlari va Innovatsion rivojlanish kengashi orqali",
            parse_mode='Markdown'
        )

    elif text == "🌐 Hamkorlik":
        bot.send_message(message.chat.id,
            "🌐 Xalqaro hamkorlik:\n"
            "- AQSH, Xitoy, Yaponiya kabi davlatlar bilan\n"
            "- Ilg‘or ta’lim dasturlari\n"
            "- Xorijiy mutaxassislar jalb etiladi",
            parse_mode='Markdown'
        )

    elif text == "📞 Aloqa":
        bot.send_message(message.chat.id,
            "📞 Aloqa uchun telefon raqamlari:\n"
            "+998 (55) 888-55-55\n"
            "+998 95 182 71 17\n\n"
            "📍 Universitet manzili:\n"
            "Toshkent viloyati, Nurafshon shahri."
        )

    elif text == "🔙 Orqaga":
        main_menu_uz(message.chat.id)

    else:
        bot.send_message(message.chat.id, "Iltimos, menyudan tanlang.")

def russian_sections(message):
    text = message.text

    if text == "ℹ️ О университете":
        bot.send_message(message.chat.id,
           
