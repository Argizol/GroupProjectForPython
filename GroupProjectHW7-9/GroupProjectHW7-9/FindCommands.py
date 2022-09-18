from Contacts import data
from phonebook_bot import bot

def find_contact(user_data):
    global data
    number = 0
    filtered_list = []
    for name, phone in data.items():
        if (user_data in name) or (user_data in phone):
            filtered_list.append(f'{name},{phone}')
            number += 1
            print(f'{number} {name}, {phone}')
    return filtered_list

def find_contact_bot():
    global data
    filtered_list = []
    count = 0
    for name, phone in data.items():
        if (user_data in name) or (user_data in phone):
            filtered_list.append(f'{name},{phone}')
    keyboard = types.InlineKeyboardMarkup()
    for i in filtered_list:
            count+=1
            button = types.InlineKeyboardButton(text=filtered_list[i], callback_data= count)
            keyboard.add(count)

    #question = f'Фамилия и имя: {name} {surname}, телефон {str(phonenumber)}. Все верно?'
    #bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
