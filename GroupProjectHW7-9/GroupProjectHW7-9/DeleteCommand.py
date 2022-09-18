from Contacts import data
from Contacts import filtered_list
import logger as Log


def delete_contact(user_data):
    global data
    for name, phone in data.copy().items():
        if phone == user_data:
            del data[name]
            Log.del_logger(f'{name} {phone}')
