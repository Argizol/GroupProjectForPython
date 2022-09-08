from Contacts import data
def Add(name, surname, phonenumber):
    global data
    data[f'{name} {surname}'] = phonenumber
    return data
     





