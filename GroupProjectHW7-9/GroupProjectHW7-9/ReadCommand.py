from Contacts import data

def ReadFhoneBook(data):
    for a, b in sorted(data.items()):
        print(a, b, sep=', ')



