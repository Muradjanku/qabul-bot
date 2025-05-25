import telebot
import os
from flask import Flask, request

TOKEN = "7797937191:AAHJBPfOQVKLB0wzMiVKQoncVeTWvSWmyn0"
WEBHOOK_DOMAIN = "https://cyber-uni-bot.up.railway.app"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Boshlang‘ich menyu
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("ℹ️ Universitet haqida", "📚 Ta’lim yo‘nalishlari")
    markup.add("🎓 O‘quv tizimi", "💰 Grant va stipendiyalar")
    markup.add("🌐 Hamkorlik", "📍Joylashuv")
    bot.send_message(message.chat.id, "Cyber University qabul botiga xush kelibsiz!\nTanlang:", reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "ℹ️ Universitet haqida")
def university_info(msg):
    bot.send_message(msg.chat.id,
        "⚙️ *Cyber University* — O‘zbekistonning raqamli kelajagiga yo‘l ochuvchi zamonaviy oliy ta’lim dargohi.\n\n"
        "📅 *Tashkil etilgan:* 2025-yil 20-yanvar\n"
        "📄 *Asos:* [PQ–14-sonli qaror](https://lex.uz/uz/docs/-7332592)\n\n"
        "🎯 *Maqsad:* xalqaro raqobatbardosh, innovatsion fikrlovchi va amaliy ko‘nikmaga ega Kiberxavfsizlik mutaxassislarini tayyorlash.",
        parse_mode='Markdown'
    )

@bot.message_handler(func=lambda msg: msg.text == "📚 Ta’lim yo‘nalishlari")
def programs_info(msg):
    bot.send_message(msg.chat.id,
        "📚 *Bakalavriat yo‘nalishlari:*\n\n"
        "1. *Kiberxavfsizlik injiniringi* – Tarmoq, tizim va internet ashyolari xavfsizligi.\n"
        "2. *Kompyuter injiniringi* – Sun’iy intellekt, algoritmlar, kompyuter tizimlari.\n"
        "3. *Dasturiy injiniring* – Amaliy matematika, dasturlash va muhandislik.\n"
        "4. *Yurisprudensiya* – Kiber huquq va raqamli kriminalistika.\n"
        "5. *Menejment* – Kiberxavfsizlik strategiyasi va risk menejmenti.\n"
        "6. *Iqtisodiyot* – Raqamli iqtisodiyot, fintech va blockchain asoslari.\n\n"
        "📚 *Magistratura yo‘nalishlari:*\n\n"
        "- Axborot xavfsizligi\n"
        "- Kiber huquq\n\n"
        "🔗 Batafsil: https://csu.uz/uz/education/programs",
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

# Webhook POST
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

# Webhook sozlash
@app.route('/set_webhook', methods=['GET'])
def set_webhook():
    webhook_url = f"{WEBHOOK_DOMAIN}/{TOKEN}"
    if bot.set_webhook(url=webhook_url):
        return f"Webhook o‘rnatildi: {webhook_url}"
    else:
        return "Webhook o‘rnatilmadi"

@app.route('/', methods=['GET'])
def index():
    return "Cyber University bot ishlayapti."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
