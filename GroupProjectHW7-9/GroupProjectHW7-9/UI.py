from aifc import Error # нахера нам этот импорт?
import logger as Log
import AddCommand as Add
import ReadCommand as Read
import DeleteCommand as Del
import EditCommand as Edit
import ExitCommand as Exit
import FindCommands as Find
import ImportFile as Import
import ExportFile as Export
import re
from Contacts import data


def menu():
    global data
    can_work = True
    command_import = input('Добро пожаловать в телефонный справочник\nХотите импортировать файл? Да/нет: ').lower()
    if command_import in ('да', 'lf', 'yes', 'y', 'д', 'l'):
        data = Import.import_from_file()
    while can_work:
        try:
            command = input('Введите команду:'
                            '\n"Add" - чтобы добавить новый контакт,'
                            '\n"Del" - чтобы удалить контакт,'
                            '\n"Find" - чтобы найти контакт,'
                            '\n"Read" - чтобы вывести на экран весь справочник,'
                            '\n"Exit" - чтобы выйти из приложения.\n').capitalize()
            match command:
                case 'Add':
                    name = ''
                    surname = ''
                    phonenumber = ''
                    while not name.isalpha():
                        name = input('Введите имя: ').capitalize()
                        if not name.isalpha():
                            print('Имя может состоять только из русских или латинских букв')
                    while not surname.isalpha():
                        surname = input('Введите фамилию: ').capitalize()
                        if not surname.isalpha():
                            print('Фамилия может состоять только из русских или латинских букв')
                    while not phonenumber.isdigit():
                        phonenumber = input('Введите номер телефона: ')
                        if not phonenumber.isdigit():
                            print('Номер телефона может включать только цифры')
                    Add.add(name, surname, phonenumber)
                    print('Абонент сохранен в справочник.')
                case 'Read':
                    Read.read_phone_book() if len(data) > 0 else print('Телефонный справочник пуст.')
                case 'Del':
                    user = input('Какой контакт Вы хотите удалить? Введите имя абонента или номер телефона: ')
                    user_pool = list(Find.find_contact(user))
                    if len(user_pool) > 1:
                        user_choice = int(input('Для выбора нужного контакта введите его порядковый номер: '))
                        user_for_commands = user_pool[user_choice - 1].split(',')
                        print(user_pool[user_choice - 1])
                        Del.delete_contact(user_for_commands[1])
                        print(f'Запись абонента {user_for_commands[0]}, {user_for_commands[1]} удалена.')
                    elif len(user_pool) == 1:
                        user_for_commands = user_pool[0].split(',')
                        Del.delete_contact(user_for_commands[1])
                        print(f'Запись абонента {user_for_commands[0]}, {user_for_commands[1]} удалена.')
                    else:
                        print('Пользователи не найдены.')
                case 'Find':
                    while True:
                        user = input('Какой контакт Вы хотите найти? ')
                        user_pool = list(Find.find_contact(user))
                        if len(user_pool) > 1:
                            user_choice = int(input('Для выбора нужного контакта введите его порядковый номер: '))
                            user_for_commands = user_pool[user_choice - 1].split(',')
                            print(user_pool[user_choice - 1])
                        elif len(user_pool) == 1:
                            user_for_commands = user_pool[0].split(',')
                        else:
                            print('Пользователи не найдены. ')
                        command_for_edit = input('Введите дальнейшую команду:'
                                                 '\nEdit - для изменения контакта'
                                                 '\nDel - для удаления контакта'
                                                 '\nExit - для выхода в главное меню.\n').capitalize()
                        match command_for_edit:
                            case 'Edit':
                                new_data = input('Введите новое значение имени/телефона: ')
                                if re.compile("^[0-9\s()+-]*$").match(new_data):
                                    Edit.change_contact_number(user_for_commands[0], new_data)
                                elif re.compile("^[a-zA-ZА-Яа-я\s]*$").match(new_data):
                                    Edit.change_contact_name(user_for_commands[0], new_data)
                                else:
                                    print('Вы ввели некорректное значение')
                            case 'Del':
                                Del.delete_contact(user_for_commands[1])
                                print(f'Запись абонента {user_for_commands[0]}, {user_for_commands[1]} удалена.')
                            case 'Exit':
                                break  
                            case _:
                                print("Введены неправильные данные. Повторите ввод команды. ")
                        user_pool.clear()
                case 'Exit':
                    export = input('Сохранить файл телефонного справочника?\nДа/нет: ').lower()
                    if export in ('да', 'lf', 'yes', 'нуы', 'y', 'н', 'д', 'l'):
                        Export.export_contacts(data)
                        print('Телефонный справочник успешно экспортирован!')
                    print('Работа завершена.')
                    can_work = Exit.exit(can_work)
                case _:
                    print("Введены неправильные данные. Повторите ввод команды. ")
        except Exception as error:
            print("Введены неправильные данные. Перезапуск приложения...")
            Log.error_logger(error)
