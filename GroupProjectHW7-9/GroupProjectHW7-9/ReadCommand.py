from Contacts import data


def read_phone_book():
    global data
    for name, phone in sorted(data.items()):
        print(name, phone, sep=', ')


