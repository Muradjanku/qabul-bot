import os
from telebot import TeleBot, types

bot = TeleBot(os.getenv("TELEGRAM_TOKEN"))

# /start komandasi
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ℹ️ Universitet haqida", "📚 Ta’lim yo‘nalishlari")
    markup.add("🎓 O‘quv tizimi", "💰 Grant va stipendiyalar")
    markup.add("🌐 Hamkorlik", "📍Joylashuv")
    bot.send_message(message.chat.id,
                     "Cyber University qabul botiga xush kelibsiz!\nKerakli bo‘limni tanlang:",
                     reply_markup=markup)

# /help komandasi
@bot.message_handler(commands=['help'])
def help_command(message):
    text = (
        "/start - Botni ishga tushirish\n"
        "/help - Qo‘llanma va yordam\n"
        "ℹ️ Universitet haqida - Umumiy ma’lumot\n"
        "📚 Ta’lim yo‘nalishlari - Batafsil yo‘nalishlar\n"
        "🎓 O‘quv tizimi - Ta’lim jarayoni haqida\n"
        "💰 Grant va stipendiyalar - Imkoniyatlar\n"
        "🌐 Hamkorlik - Xalqaro hamkorlik\n"
        "📍 Joylashuv - Universitet manzili\n"
    )
    bot.send_message(message.chat.id, text)

# ℹ️ Universitet haqida
@bot.message_handler(func=lambda m: m.text == "ℹ️ Universitet haqida")
def university_info(message):
    text = (
        "⚙️ Cyber University — O‘zbekistonning raqamli kelajagiga yo‘l ochuvchi zamonaviy oliy ta’lim dargohi.\n\n"
        "O‘zbekiston Respublikasi Prezidentining 2025-yil 20-yanvardagi PQ–14-sonli qaroriga asosan — Cyber University tashkil etildi.\n\n"
        "Qarorni o‘qing! 🫵 https://lex.uz/uz/docs/-7332592\n\n"
        "🫥 Asosiy maqsad:\n"
        "Cyber University xalqaro raqobatbardosh, innovatsion fikrlovchi va amaliy ko‘nikmaga ega "
        "Kiberxavfsizlik mutaxassislarini tayyorlashga yo‘naltirilgan."
    )
    bot.send_message(message.chat.id, text)

# 📚 Ta’lim yo‘nalishlari (batafsil)
@bot.message_handler(func=lambda m: m.text == "📚 Ta’lim yo‘nalishlari")
def education_programs(message):
    programs = {
        "Kiberxavfsizlik injiniringi": "Tarmoq va tizim xavfsizligi, himoya vositalari va xavfsizlik texnologiyalari.",
        "Kompyuter injiniringi": "Sun’iy intellekt, ma’lumotlarni qayta ishlash, algoritmlar va dasturlash.",
        "Dasturiy injiniring": "Amaliy matematika, algoritmlashtirish, dasturiy ta'minot ishlab chiqish.",
        "Yurisprudensiya": "Kiber huquq, raqamli kriminalistika, qonunchilik asoslari.",
        "Menejment": "Kiberxavfsizlik menejmenti, loyiha boshqaruvi va tashkilot boshqaruvi.",
        "Iqtisodiyot": "Raqamli iqtisodiyot, elektron tijorat va moliyaviy texnologiyalar."
    }

    text = "📚 *Bakalavriat yo‘nalishlari va batafsil ma’lumot:*\n\n"
    for prog, desc in programs.items():
        text += f"• *{prog}*\n  {desc}\n\n"

    text += "Qo‘shimcha ma’lumotlar uchun rasmiy saytga murojaat qiling: https://cyberuniversity.uz/programs"
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# Qo‘shimcha menyu punktlar uchun (misol sifatida)
@bot.message_handler(func=lambda m: m.text == "🎓 O‘quv tizimi")
def education_system(message):
    text = (
        "🎓 *O‘quv jarayoni xususiyatlari:*\n"
        "- 1 yil Foundation, 3 yil asosiy ta’lim\n"
        "- Ta’lim to‘liq ingliz tilida\n"
        "- Kredit-modul tizimi\n"
        "- Amaliyot IT kompaniyalari va texnoparklarda\n"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "💰 Grant va stipendiyalar")
def grants(message):
    text = (
        "💰 *Imkoniyatlar:*\n"
        "- 2025/2026 o‘quv yili uchun 100 ta davlat granti\n"
        "- Stipendiyalar: sanoat hamkorlari va Innovatsion rivojlanish kengashi orqali"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "🌐 Hamkorlik")
def cooperation(message):
    text = (
        "🌐 *Xalqaro hamkorlik:*\n"
        "- AQSH, Xitoy, Yaponiya kabi davlatlar bilan\n"
        "- Ilg‘or ta’lim dasturlari\n"
        "- Xorijiy mutaxassislar jalb etiladi"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "📍Joylashuv")
def location(message):
    bot.send_message(message.chat.id, "📍 Universitet: Toshkent viloyati, Nurafshon shahri.")

# Default javob
@bot.message_handler(func=lambda m: True)
def default_response(message):
    bot.send_message(message.chat.id, "Savolingizni tushunmadim. /help buyrug‘ini bering yoki menyudan tanlang.")

bot.infinity_polling()
