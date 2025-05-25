from telebot import TeleBot, types
import os

bot = TeleBot(os.getenv("TELEGRAM_TOKEN"))

# Global dictionary for user language: {chat_id: 'uz' or 'ru'}
user_lang = {}

# Asosiy menyu tugmalari (tilga qarab o‘zgaradi)
def main_menu(lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if lang == 'ru':
        markup.add("ℹ️ О университете", "📚 Направления обучения")
        markup.add("🎓 Учебная система", "💰 Гранты и стипендии")
        markup.add("🌐 Партнёрство", "📍Расположение")
        markup.add("📞 Контакты")
    else:
        markup.add("ℹ️ Universitet haqida", "📚 Ta’lim yo‘nalishlari")
        markup.add("🎓 O‘quv tizimi", "💰 Grant va stipendiyalar")
        markup.add("🌐 Hamkorlik", "📍Joylashuv")
        markup.add("📞 Aloqa uchun")
    return markup

# Til tanlash menyusi
def lang_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🇺🇿 O‘zbekcha", "🇷🇺 Русский")
    return markup

# Orqaga tugma (Tilga qarab)
def back_button(lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if lang == 'ru':
        markup.add("⬅️ Назад", *main_menu('ru').keyboard[0])
    else:
        markup.add("⬅️ Orqaga", *main_menu('uz').keyboard[0])
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_lang[message.chat.id] = 'uz'  # Default til - o‘zbekcha
    bot.send_message(message.chat.id, "Tilni tanlang / Выберите язык", reply_markup=lang_menu())

@bot.message_handler(func=lambda msg: msg.text in ["🇺🇿 O‘zbekcha", "🇷🇺 Русский"])
def set_language(msg):
    if msg.text == "🇺🇿 O‘zbekcha":
        user_lang[msg.chat.id] = 'uz'
        bot.send_message(msg.chat.id, "Til o‘zbekcha sifatida tanlandi.", reply_markup=main_menu('uz'))
    else:
        user_lang[msg.chat.id] = 'ru'
        bot.send_message(msg.chat.id, "Язык выбран: русский.", reply_markup=main_menu('ru'))

@bot.message_handler(func=lambda msg: msg.text in [
    "ℹ️ Universitet haqida", "📚 Ta’lim yo‘nalishlari", "🎓 O‘quv tizimi",
    "💰 Grant va stipendiyalar", "🌐 Hamkorlik", "📍Joylashuv", "📞 Aloqa uchun",
    "ℹ️ О университете", "📚 Направления обучения", "🎓 Учебная система",
    "💰 Гранты и стипендии", "🌐 Партнёрство", "📍Расположение", "📞 Контакты",
    "⬅️ Orqaga", "⬅️ Назад"
])
def handle_menu(msg):
    lang = user_lang.get(msg.chat.id, 'uz')
    text = msg.text

    # Orqaga tugma
    if text in ["⬅️ Orqaga", "⬅️ Назад"]:
        bot.send_message(msg.chat.id,
                         "Asosiy menyu" if lang == 'uz' else "Главное меню",
                         reply_markup=main_menu(lang))
        return

    # O‘zbekcha menyu
    if lang == 'uz':
        if text == "ℹ️ Universitet haqida":
            bot.send_message(msg.chat.id,
                "⚙️ Cyber University — O‘zbekistonning raqamli kelajagiga yo‘l ochuvchi zamonaviy oliy ta’lim dargohi.\n\n"
                "O‘zbekiston Respublikasi Prezidentining 2025-yil 20-yanvardagi PQ–14-sonli qaroriga asosan — Cyber University tashkil etildi.\n\n"
                "Qarorni o‘qing! 🫵https://lex.uz/uz/docs/-7332592\n\n"
                "🫥 Asosiy maqsad\n"
                "Cyber University xalqaro raqobatbardosh, innovatsion fikrlovchi va amaliy ko‘nikmaga ega kiberxavfsizlik mutaxassislarini tayyorlashga yo‘naltirilgan.",
                reply_markup=back_button('uz'))
        elif text == "📚 Ta’lim yo‘nalishlari":
            bot.send_message(msg.chat.id,
                "📚 *Bakalavriat yo‘nalishlari:*\n"
                "- Kiberxavfsizlik injiniringi\n"
                "  — Tarmoq va tizim xavfsizligini ta’minlash, kiberhujumlarga qarshi kurashish.\n"
                "- Kompyuter injiniringi\n"
                "  — Sun’iy intellekt, dasturiy ta’minot yaratish va optimallashtirish.\n"
                "- Dasturiy injiniring\n"
                "  — Amaliy matematika, algoritmlashtirish va dasturiy mahsulotlar ishlab chiqish.\n"
                "- Yurisprudensiya\n"
                "  — Kiber huquq, raqamli kriminalistika va axborot xavfsizligi qonunlari.\n"
                "- Menejment\n"
                "  — Kiberxavfsizlik menejmenti, IT loyihalarni boshqarish.\n"
                "- Iqtisodiyot\n"
                "  — Raqamli iqtisodiyot, innovatsion biznes-modellar.\n\n"
                "🎓 *Magistratura yo‘nalishlari:*\n"
                "- Axborot xavfsizligi\n"
                "  — Axborot tizimlarini himoya qilish, tarmoq xavfsizligi va kiberxavfsizlik texnologiyalari.\n"
                "- Kiber huquq\n"
                "  — Kiberjinoyatchilikka qarshi qonunchilik, shaxsiy ma’lumotlarni himoya qilish va raqamli huquq.\n",
                parse_mode='Markdown', reply_markup=back_button('uz'))
        elif text == "🎓 O‘quv tizimi":
            bot.send_message(msg.chat.id,
                "🎓 *O‘quv jarayoni xususiyatlari:*\n"
                "- 1 yil Foundation, 3 yil asosiy ta’lim\n"
                "- Ta’lim to‘liq ingliz tilida\n"
                "- Kredit-modul tizimi\n"
                "- Amaliyot IT kompaniyalari va texnoparklarda",
                parse_mode='Markdown', reply_markup=back_button('uz'))
        elif text == "💰 Grant va stipendiyalar":
            bot.send_message(msg.chat.id,
                "💰 *Imkoniyatlar:*\n"
                "- 2025/2026 o‘quv yili uchun 100 ta davlat granti\n"
                "- Stipendiyalar: sanoat hamkorlari va Innovatsion rivojlanish kengashi orqali",
                parse_mode='Markdown', reply_markup=back_button('uz'))
        elif text == "🌐 Hamkorlik":
            bot.send_message(msg.chat.id,
                "🌐 *Xalqaro hamkorlik:*\n"
                "- AQSH, Xitoy, Yaponiya kabi davlatlar bilan\n"
                "- Ilg‘or ta’lim dasturlari\n"
                "- Xorijiy mutaxassislar jalb etiladi",
                parse_mode='Markdown', reply_markup=back_button('uz'))
        elif text == "📍Joylashuv":
            bot.send_message(msg.chat.id,
                "📍 Universitet: Toshkent viloyati, Nurafshon shahri.",
                reply_markup=back_button('uz'))
        elif text == "📞 Aloqa uchun":
            bot.send_message(msg.chat.id,
                "📞 Aloqa uchun:\n+998 (55) 888-55-55\n+998951827117",
                reply_markup=back_button('uz'))

    # Ruscha menyu
    else:
        if text == "ℹ️ О университете":
            bot.send_message(msg.chat.id,
                "⚙️ Cyber University — современное высшее учебное заведение, открывающее цифровое будущее Узбекистана.\n\n"
                "Основан на основании постановления Президента Республики Узбекистан от 20 января 2025 года № PQ–14.\n\n"
                "Читайте постановление! 🫵https://lex.uz/uz/docs/-7332592\n\n"
                "🫥 Основная цель\n"
                "Cyber University направлен на подготовку специалистов по кибербезопасности с международной конкурентоспособностью, инновационным мышлением и практическими навыками.",
                reply_markup=back_button('ru'))
        elif text == "📚 Направления обучения":
            bot.send_message(msg.chat.id,
                "📚 *Бакалавриат:*\n"
                "- Инженерия кибербезопасности\n"
                "  — Обеспечение безопасности сетей и систем, противодействие кибератакам.\n"
                "- Компьютерная инженерия\n"
                "  — Искусственный интеллект, разработка и оптимизация программного обеспечения.\n"
                "- Программная инженерия\n"
                "  — Прикладная математика, алгоритмизация и разработка ПО.\n"
                "- Юриспруденция\n"
                "  — Киберправо, цифровая криминалистика и законодательство по информационной безопасности.\n"
                "- Менеджмент\n"
                "  — Управление кибербезопасностью, управление IT-проектами.\n"
                "- Экономика\n"
                "  — Цифровая экономика, инновационные бизнес-модели.\n\n"
                "🎓 *Магистратура:*\n"
                "- Информационная безопасность\n"
                "  — Защита информационных систем, безопасность сетей и технологии кибербезопасности.\n"
                "- Киберправа\n"
                "  — Законодательство против киберпреступности, защита персональных данных и цифровое право.\n",
                parse_mode='Markdown', reply_markup=back_button('ru'))
        elif text == "🎓 Учебная система":
            bot.send_message(msg.chat.id,
                "🎓 *Особенности учебного процесса:*\n"
                "- 1 год Foundation, 3 года основного обучения\n"
                "- Обучение полностью на английском языке\n"
                "- Кредитно-модульная система\n"
                "- Практика в IT-компаниях и технопарках",
                parse_mode='Markdown', reply_markup=back_button('ru'))
        elif text == "💰 Гранты и стипендии":
            bot.send_message(msg.chat.id,
                "💰 *Возможности:*\n"
                "- 100 государственных грантов на 2025/2026 учебный год\n"
                "- Стипендии через партнеров промышленности и Совет инновационного развития",
                parse_mode='Markdown', reply_markup=back_button('ru'))
        elif text == "🌐 Партнёрство":
            bot.send_message(msg.chat.id,
                "🌐 *Международное сотрудничество:*\n"
                "- Соединённые Штаты, Китай, Япония и другие страны\n"
                "- Современные образовательные программы\n"
                "- Привлечение иностранных специалистов",
                parse_mode='Markdown', reply_markup=back_button('ru'))
        elif text == "📍Расположение":
            bot.send_message(msg.chat.id,
                "📍 Университет: Ташкентская область, город Нурафшон.",
                reply_markup=back_button('ru'))
        elif text == "📞 Контакты":
            bot.send_message(msg.chat.id,
                "📞 Контакты:\n+998 (55) 888-55-55\n+998951827117",
                reply_markup=back_button('ru'))

bot.infinity_polling()
