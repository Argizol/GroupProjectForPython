from email import message_from_string
from email.message import Message
import telebot
import logger as Log
import AddCommand as Add
import ReadCommand as Read
import DeleteCommand as Del
import EditCommand as Edit
import ExitCommand as Exit
import FindCommands as Find
import ImportFile as Import
import ExportFile as Export
import re
from Contacts import data

# Создаем экземпляр бота
bot = telebot.TeleBot('5702651173:AAEhqZS4TNEXRaUV6dJeW9K4OnuN8KZ-iZs')
def get_name(message):
    global name
    name = message.text


def get_surname(message):
    global surname
    surname = message.text


def get_phonenumber(message):
    global phonenumber
    phonenumber = message.text

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

@bot.message_handler(content_types=[
    "audio", "photo", "sticker", "video",
    "video_note", "voice", "location", "contact",
    "new_chat_members", "left_chat_member", "new_chat_title",
    "new_chat_photo", "delete_chat_photo", "group_chat_created",
    "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
    "migrate_from_chat_id", "pinned_message", "web_app_data"
    ])
def warning(message):
    bot.send_message(message.chat.id, f'Я тебя не понимаю. Введи: /help.')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def start_menu(message):
    data = Import.import_from_file()
    #bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    match message.text:
         case '/Read':
             if len(data) > 0:
                Read.read_phone_book()               
             else: 
                print('Телефонный справочник пуст.')
        #case "/Add":
        #    name = ''
        #    surname = ''
        #    phonenumber = ''
        #    #if not name.isalpha():
        #    msg = bot.send_message(message.chat.id,'Введите имя')
        #    bot.register_next_step_handler(msg, get_name)
        #        #bot.register_next_step_handler(msg, get_name)                
        #        #if not name.isalpha():
        #            #bot.send_message(message.chat.id,'Имя может состоять только из русских или латинских букв')
        #    ##while not surname.isalpha():
        #    #    bot.reply_to(message,'Введите фамилию: ')
        #    #    bot.register_next_step_handler(message, get_surname)
        #    #    if not surname.isalpha():
        #    #        bot.send_message(message.chat.id,'Фамилия может состоять только из русских или латинских букв')
        #    ##while not phonenumber.isdigit():
        #    #    bot.reply_to(message,'Введите номер телефона')
        #    #    bot.register_next_step_handler(message, get_phonenumber) 
        #    #    if not phonenumber.isdigit():
        #    #        bot.send_message(message.chat.id,'Номер телефона может включать только цифры')
        #    Add.add(name, surname, phonenumber)
        #    bot.send_message(message.chat.id,'Абонент сохранен в справочник')


# Постоянная проверка новых сообщений
bot.polling(none_stop=True, interval=0)


    