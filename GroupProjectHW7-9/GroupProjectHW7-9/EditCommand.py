import logger as Log
from Contacts import data


def change_contact_number(old_data, new_data):
    global data
    data[old_data] = new_data
    #print(f'Номер абонента {old_data} изменен. Новый номер: {new_data}')
    Log.edit_logger(f'{old_data} changed number to {new_data}')
    return data


def change_contact_name(old_data, new_data):
    global data
    data[new_data] = data.pop(old_data)
    #print(f'Имя абонента {old_data} изменено. Новое имя: {new_data}')
    Log.edit_logger(f'{old_data} changed name to {new_data}')
    return data
