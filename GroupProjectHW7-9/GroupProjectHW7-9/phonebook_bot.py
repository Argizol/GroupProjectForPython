import telebot
from telebot import types

#name for your bot - phonebook_bot
#username for your bot - python_phonebook_bot

TOKEN = '5702651173:AAEhqZS4TNEXRaUV6dJeW9K4OnuN8KZ-iZs'

bot = telebot.TeleBot(TOKEN)

name = ''
surname = ''
number = 0


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'start':
        bot.send_message(message.from_user.id, 'Введите имя: ')
        bot.register_next_step_handler(message, dialog1)
    else:
        bot.send_message(message.from_user.id, 'Проверьте ввод')


def dialog1(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Введите фамилию: ')
    bot.register_next_step_handler(message, dialog2)


def dialog2(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Введите номер телефона: ')
    bot.register_next_step_handler(message, dialog3)


def dialog3(message):
    global number
    number = message.text

    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(yes)
    no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(no)

    question = f'Фамилия и имя: {name} {surname}, телефон {str(number)}. Все верно?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Отлично!')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Печалька')
        bot.send_message(call.message.chat.id, 'Введите /start для перезапуска бота')


bot.polling(none_stop=True, interval=0)
    