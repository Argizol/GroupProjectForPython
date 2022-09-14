import AddCommand as Add
import ReadCommand as Read
import DeleteCommand as Del
import EditCommand as Edit
import ExitCommand as Exit
import FindCommands as Find
import ImportFile as Import
import ExportFile as Export
from Contacts import data


def Menu():
    global data
    canWork = True
    command_import = input('Добро пожаловать в телефонный справочник\nХотите импортировать файл? Да/нет: ').lower()
    if command_import == 'да':
        data = Import.ImportFromFile()  # надо прикрутить в метод указание пути, где лежит файл для импорта.
    while canWork:
        # try:
        command = input('Введите команду:'
                        '\n"Add" - чтобы добавить новый контакт,'
                        '\n"Del" - чтобы удалить контакт,'
                        '\n"Find" - чтобы найти контакт,'
                        '\n"Exit" - чтобы выйти из приложения.\n')
        match command:
            case 'Add':
                name = ''
                surname = ''
                phonenumber = ''
                while not name.isalpha():
                    name = input('Введите имя: ')
                    if not name.isalpha():
                        print('Имя может состоять только из русских или латинских букв')
                while not surname.isalpha():
                    surname = input('Введите фамилию: ')
                    if not surname.isalpha():
                        print('Фамилия может состоять только из русских или латинских букв')
                while not phonenumber.isdigit():
                    phonenumber = input('Введите номер телефона:')
                    if not phonenumber.isdigit():
                        print('Номер телефона может включать только цифры')
                Add.Add(name, surname, phonenumber)  # Реализовать разбиение сплитом на список
                print('Абонент сохранен в справочник.')

            case 'Read':
                Read.ReadFhoneBook() if len(data) > 0 else print('The phonebook is empty.') # Проверка на пустой словарь
            case 'Del':
                user = input('Кого Вы хотите удалить? Введите ФИО или номер телефона')
                user_pool = list(Find.Find(user))
                if len(user_pool) > 1:
                    user_choice = int(input('Пользователя под каким номером Вы хотите выбрать?'))
                    user_for_commands = user_pool[user_choice - 1].split(',')
                    print(user_pool[user_choice - 1])
                    Del.Delete(user_for_commands[1])
                elif len(user_pool) == 1:
                    user_for_commands = user_pool[0].split(',')
                    Del.Delete(user_for_commands[1])
                else:
                    print('Пользователи не найдены. ')              
            #case 'Edit':
            #    user = input('Какой контакт Вы хотите изменить?')
            #    Edit.EditByName(user)
            #    Edit.EditByPhoneNumber(user)
            #    Edit.EditBySurname(user)
            case 'Find':
                user = input('Какой контакт Вы хотите найти?')

                user_pool = list(Find.Find(user))  # проверка на ввод и вызов нужного метода
                if len(user_pool) > 1:
                    user_choice = int(input('Пользователя под каким номером Вы хотите выбрать?'))
                    user_for_commands = user_pool[user_choice - 1].split(',')
                    print(user_pool[user_choice - 1])
                elif len(user_pool) == 1:
                    user_for_commands = user_pool[0].split(',')
                else:
                    print('Пользователи не найдены. ')
                command_for_edit = input(
                    'Введите дальнейшую команду:\nEdit - для изменения контакта\nDel - для удаления контакта\nExit - для выхода вглавное меню.\n')
                match command_for_edit:
                    #case 'Edit':
                    #    123
                    #    # Нужно нарисовать команду Edit.
                    case 'Del':
                        Del.Delete(user_for_commands[1])
                    case 'Exit':
                        break  # ? хз как это будет тут работать, надо потестить и сделать выход в меню.
                    case _:
                        print("Введены неправильные данные. Повторите ввод команды. ")
                user_pool.clear()
            case 'Exit':
                export = input('Хотите экспортировать файл телефонного справочника?\nДа/нет: ').lower()
                if export == 'да':
                    Export.ExportContacts(data)
                print('Завершение работы приложения...')
                Exit.Exit(canWork)  # а надо ли вообще отдельный метод, если можно просто присвоить тут False?
            case _:
                print("Введены неправильные данные. Повторите ввод команды. ")
    # except:
    #    print("Введены неправильные данные. Перезапуск приложения...")
