import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7945560732:AAGpQJBXfB7uldG26mesMg1RsvEz3bNnwgU'  # حط التوكن ديالك هنا
bot = telebot.TeleBot(TOKEN)

MINI_APP_URL = "https://yourgithubusername.github.io/yourrepo/index.html"  # رابط صفحتك في GitHub Pages أو استضافة أخرى

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="🚀 شاهد فتيات جميلات", web_app={"url": MINI_APP_URL}))
    bot.send_message(message.chat.id,
                     "مرحبا! اضغط على الزر أسفله لعرض فتيات جميلات بانتظارك.",
                     reply_markup=markup)

bot.polling()
