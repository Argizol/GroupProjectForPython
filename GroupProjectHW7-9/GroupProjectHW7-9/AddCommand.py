from Contacts import data
import logger as Log

def Add(name, surname, phonenumber):
    global data
    data[f'{name} {surname}'] = phonenumber
    Log.Add_logger(f'{name} {surname} {phonenumber}')
    return data
     





