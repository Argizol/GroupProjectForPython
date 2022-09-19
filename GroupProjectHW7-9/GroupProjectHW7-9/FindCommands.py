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

