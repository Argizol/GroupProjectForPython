from Contacts import data
import logger as Log


def add(name, surname, phonenumber):
    global data
    data[f'{name} {surname}'] = phonenumber
    Log.add_logger(f'{name} {surname} {phonenumber}')
    return data
     





