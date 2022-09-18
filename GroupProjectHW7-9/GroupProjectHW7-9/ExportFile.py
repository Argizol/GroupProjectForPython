def export_contacts(data):
    with open(r'phonebook.csv', 'a+') as f:
        for x, y in data.items():
            f.write(f'{x}, {y}\n')
    




