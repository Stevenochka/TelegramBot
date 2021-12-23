import telebot
from telebot import types

token = "2136292196:AAHOZjfe2RC-nDVdm4iW2VYWW96GNu2xXyE"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "Не хочу", "Да", "Нет", "/help", "/directions", "/start")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['directions'])
def start_message(message):
    bot.send_message(message.chat.id, 'Тебя интересуют напрявления подготовки?')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею\n/start - свежая информация о ВУЗе\n/directions - направления подготовки'
                                      '\n/help - сводка комманд')




@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "не хочу":
        bot.send_message(message.chat.id, 'Тогда мне нечем помочь тебе(((')
    elif message.text.lower() == "да":
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://abitur.mtuci.ru/')
    elif message.text.lower() == "нет":
        bot.send_message(message.chat.id, 'Тогда мне нечем помочь тебе(((')


bot.polling()
