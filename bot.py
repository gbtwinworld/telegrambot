import telebot

bot = telebot.TeleBot('1167015130:AAGYYQFqz1mpndoNzRCD2ZLHinfn5vVA7Qc')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()
