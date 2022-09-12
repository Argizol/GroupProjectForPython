from Contacts import data

def ReadFhoneBook():
    global data
    for a, b in sorted(data.items()):
        print(a, b, sep=', ')



