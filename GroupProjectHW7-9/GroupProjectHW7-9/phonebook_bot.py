import telebot
from telebot import types
import ReadCommand
import AddCommand
import logger
import DeleteCommand
import EditCommand
import ExitCommand
import FindCommands
import ImportFile
import ExportFile
import re
from Contacts import data

#name for your bot - phonebook_bot
#username for your bot - python_phonebook_bot

name = ''
surname = ''
phonenumber = 0

TOKEN = '5702651173:AAEhqZS4TNEXRaUV6dJeW9K4OnuN8KZ-iZs'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #import_from_file =
    #export_contacts =
    read_phone_book = types.KeyboardButton('Вывести справочник на экран')
    find_contact = types.KeyboardButton('Найти контакт')
    add_contact = types.KeyboardButton('Добавить контакт')
    delete_contact = types.KeyboardButton('Удалить контакт')
    change_contact = types.KeyboardButton('Редактировать контакт')

    markup.add(read_phone_book, find_contact, add_contact, delete_contact, change_contact)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Вывести справочник на экран':
            for i,j in data.items():
                bot.send_message(message.from_user.id,f'{i} {j}')
        if message.text == 'Добавить контакт':
            bot.send_message(message.from_user.id, 'Введите имя: ')
            bot.register_next_step_handler(message, get_name)
        if message.text == 'Найти контакт':
            FindCommands.find_contact_bot()


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Введите фамилию: ')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Введите номер телефона: ')
    bot.register_next_step_handler(message, get_phonenumber)


def get_phonenumber(message):
    global phonenumber
    phonenumber = message.text

    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(yes)
    no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(no)

    question = f'Фамилия и имя: {name} {surname}, телефон {str(phonenumber)}. Все верно?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Отлично!')
        AddCommand.add_bot(name, surname, phonenumber)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Печалька')
        bot.send_message(call.message.chat.id, 'Введите /start для перезапуска бота')


def find_contact_bot(user_data):
    global data
    filtered_list = []
    for name, phone in data.items():
        if (user_data in name) or (user_data in phone):
            filtered_list.append(f'{name},{phone}')
    return filtered_list


bot.polling(none_stop=True)
