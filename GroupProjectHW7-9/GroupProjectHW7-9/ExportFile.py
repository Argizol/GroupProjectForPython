def export_contacts(data):
    with open(r'phonebook.csv', 'w') as f:
        for x, y in data.items():
            f.write(f'{x}, {y}\n')
    




