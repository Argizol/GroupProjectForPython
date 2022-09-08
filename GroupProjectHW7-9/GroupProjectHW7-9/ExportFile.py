def ExportContacts(data):
    with open(r'exported_phonebook.csv', 'w') as f:
        for x, y in data.items():
            f.write(f'{x}, {y}\n')
    




