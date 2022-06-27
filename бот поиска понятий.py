import telebot
import wikipedia
wikipedia.set_lang('ru')
last_five_words = []
bot = telebot.TeleBot('1871854372:AAG0Y0krQoPbSpnGxM1IzW9_8spSIOk__HI')
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Введи слово: ')
@bot.message_handler(content_types = ['text'])
def send_word(message):
    if message.text.lower() and message.text.lower() != 'история':
        try:
            last_five_words.append(message.text)
            bot.send_message(message.chat.id, {wikipedia.summary(message.text)})
            bot.send_message(message.chat.id, 'Введи слово: ')
        except:
            bot.send_message(message.chat.id, 'Попробуй еще раз: ')

bot.polling()