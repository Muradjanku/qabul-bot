from telebot import TeleBot, types
import os

bot = TeleBot(os.getenv("TELEGRAM_TOKEN"))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ℹ️ Universitet haqida", "📚 Ta’lim yo‘nalishlari")
    markup.add("🎓 O‘quv tizimi", "💰 Grant va stipendiyalar")
    markup.add("🌐 Hamkorlik", "📍Joylashuv")
    bot.send_message(message.chat.id, "Cyber University qabul botiga xush kelibsiz!\nTanlang:", reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "ℹ️ Universitet haqida")
def university_info(msg):
    bot.send_message(msg.chat.id,
        "📘 *Cyber University* – O‘zbekistonning raqamli kelajagiga yo‘l ochuvchi zamonaviy oliy ta’lim muassasasi.\n\n"
        "Tashkil etilgan: 2025-yil 20-yanvar\n"
        "Asos: [PQ–14-sonli qaror](https://lex.uz/uz/docs/-7332592)\n\n"
        "🎯 Maqsad: xalqaro raqobatbardosh, innovatsion fikrlaydigan va amaliy ko‘nikmaga ega mutaxassislarni tayyorlash.",
        parse_mode='Markdown'
    )

@bot.message_handler(func=lambda msg: msg.text == "📚 Ta’lim yo‘nalishlari")
def programs_info(msg):
    bot.send_message(msg.chat.id,
        "📚 *Bakalavriat yo‘nalishlari:*\n"
        "- Kiberxavfsizlik injiniringi\n"
        "- Kompyuter injiniringi\n"
        "- Dasturiy injiniring\n"
        "- Yurisprudensiya\n"
        "- Menejment\n"
        "- Iqtisodiyot",
        parse_mode='Markdown'
    )

@bot.message_handler(func=lambda msg: msg.text == "🎓 O‘quv tizimi")
def education_system(msg):
    bot.send_message(msg.chat.id,
        "🎓 *O‘quv jarayoni xususiyatlari:*\n"
        "- 1 yil Foundation, 3 yil asosiy ta’lim\n"
        "- Ta’lim to‘liq ingliz tilida\n"
        "- Kredit-modul tizimi\n"
        "- Amaliyot IT kompaniyalari va texnoparklarda",
        parse_mode='Markdown'
    )

@bot.message_handler(func=lambda msg: msg.text == "💰 Grant va stipendiyalar")
def grants_info(msg):
    bot.send_message(msg.chat.id,
        "💰 *Imkoniyatlar:*\n"
        "- 2025/2026 o‘quv yili uchun 100 ta davlat granti\n"
        "- Stipendiyalar: sanoat hamkorlari va Innovatsion rivojlanish kengashi orqali",
        parse_mode='Markdown'
    )

@bot.message_handler(func=lambda msg: msg.text == "🌐 Hamkorlik")
def partners_info(msg):
    bot.send_message(msg.chat.id,
        "🌐 *Xalqaro hamkorlik:*\n"
        "- AQSH, Xitoy, Yaponiya kabi davlatlar bilan\n"
        "- Ilg‘or ta’lim dasturlari\n"
        "- Xorijiy mutaxassislar jalb etiladi",
        parse_mode='Markdown'
    )

@bot.message_handler(func=lambda msg: msg.text == "📍Joylashuv")
def location_info(msg):
    bot.send_message(msg.chat.id, "📍 Universitet: Toshkent viloyati, Nurafshon shahri.")

bot.infinity_polling()
