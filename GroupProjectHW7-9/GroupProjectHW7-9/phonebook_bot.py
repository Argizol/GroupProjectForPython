import telebot
from telebot import types
import ReadCommand
import AddCommand
import logger as Log
import DeleteCommand as Delete
import ImportFile as Import
import ExportFile as Export
import re
from Contacts import data


#name for your bot - phonebook_bot
#username for your bot - python_phonebook_bot

name = ''
surname = ''
phonenumber = 0
user_choice = 0
filtered_list = []
user_for_commands = []

TOKEN = '5702651173:AAEhqZS4TNEXRaUV6dJeW9K4OnuN8KZ-iZs'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    import_from_file = types.KeyboardButton('Импорт')
    export_contacts = types.KeyboardButton('Экспорт')
    read_phone_book = types.KeyboardButton('Вывести справочник на экран')
    find_contact = types.KeyboardButton('Найти контакт')
    add_contact = types.KeyboardButton('Добавить контакт')
    delete_contact = types.KeyboardButton('Удалить контакт')
    change_contact = types.KeyboardButton('Редактировать контакт')

    markup.add(read_phone_book, find_contact, add_contact, delete_contact, change_contact, import_from_file, export_contacts)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Вывести справочник на экран':
            if len(data) == 0:
                bot.send_message(message.from_user.id,f'Никого нет')
            count = 0
            for i,j in data.items():
                count += 1
                bot.send_message(message.from_user.id,f'{count}. {i} {j}')
        elif message.text == 'Добавить контакт':
            bot.send_message(message.from_user.id, 'Введите имя: ')
            bot.register_next_step_handler(message, get_name)            
        elif message.text == 'Найти контакт':
            bot.send_message(message.from_user.id, 'Кого хотим найти?')
            bot.register_next_step_handler(message, find_contact_bot)            
        elif message.text == 'Удалить контакт':
            bot.send_message(message.from_user.id, 'Кого хотим найти?')            
            bot.register_next_step_handler(message, delete)
        elif message.text == 'Импорт':
            Import.import_from_file()
            bot.send_message(message.from_user.id, f'Импортировано {len(data)} контактов')
        elif message.text == 'Экспорт':
            a = len(data)
            Export.export_contacts(data)
            bot.send_message(message.from_user.id, f'Контакты успешно экспортированы в файл')


def delete(message):
    global data
    global filtered_list
    count = 0
    if len(data) == 0:
        bot.send_message(message.from_user.id,f'Никого нет')
    for name, phone in data.copy().items():
        if (message.text in name) or (message.text in phone):
            filtered_list.append(f'{name},{phone}')
            count += 1
            bot.send_message(message.from_user.id,f'{count}. {name}, {phone}')

    if len(filtered_list) > 1:
        bot.send_message(message.from_user.id,f'Какой номер удаляем?')
        bot.register_next_step_handler(message, get_userchoice, filtered_list)       
        

    if len(filtered_list) == 1:
        user_for_commands = filtered_list[0].split(',')
        Delete.delete_contact(user_for_commands[1])
        bot.send_message(message.from_user.id, f'Удален контакт: {filtered_list[0]}')
        filtered_list.clear()


def get_userchoice(message, filtered_list):
    global user_choice
    global user_for_commands
    user_choice = int(message.text)
    user_for_commands = filtered_list[user_choice - 1].split(',')
    Delete.delete_contact(user_for_commands[1])
    bot.send_message(message.from_user.id, f'Удален контакт: {filtered_list[user_choice - 1]}')
    filtered_list.clear()


def find_contact_bot(message):
    global data 
    global filtered_list
    count = 0
    if len(data) == 0:
        bot.send_message(message.from_user.id,f'Никого нет')
    for name, phone in data.items():
        if (message.text in name) or (message.text in phone):
            filtered_list.append(f'{name},{phone}')
            count += 1
            bot.send_message(message.from_user.id,f'{count}. {filtered_list[0]}')
            filtered_list.clear()
    

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



bot.polling(none_stop=True)
