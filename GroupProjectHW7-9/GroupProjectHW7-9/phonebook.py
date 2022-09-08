# указываем путь к файлу импорта
import_path = 'd:\GroupProjectForPython\phonebook.csv'
with open(import_path, 'r') as f:
    imported_phonebook = f.read().strip()
data = {}
for i in imported_phonebook.split('\n'):
    i = i.strip().split(',')
    data[i[0]] = i[1]
print(f'The phonebook from {import_path} has been successfully imported.')

# печать полученного словаря
# print(data)
# печать значения для указанного ключа: 'Green Maria': '00441202898'
# print(data.get('Green Maria'))
# print(len(data)) # длина словаря
# добавление элементов в словарь:
# data[key] = value, f.e data['ambulance'] = 112
# изменение элементов словаря
# data[key] = new_value, f.e. data['ambulance'] = 03
# удаление элементов словаря по ключу:
# del data[key], f.e. del data['ambulance'] либо
# data.pop(key), f.e. data.pop('ambulance')
# удаление последнего элемента словаря:
# data.popitem()
# # поиск по совпадению цифр в номере телефона
# for j, k in data.items():
#     if k.__contains__('00'):
#         print(j, k, sep=', ')
# # поиск по совпадению в имени:
# for j, k in data.items():
#     if j.startswith('Mo'):
#         print(j, k, sep=', ')
# # печать сортированного по алфавиту справочника:
# for a, b in sorted(data.items()):
#     print(a, b, sep=', ')

# экспортируем справочник в файл после работы с ним:
export_path = 'd:\GroupProjectForPython\exported_phonebook.csv'
with open(export_path, 'w') as f:
    for x, y in data.items():
        f.write(f'{x}, {y}\n')
print(f'The phonebook has been successfully imported to {export_path}.')
