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
    command_import = input('Добро пожаловать в телефонный справочник\n Хотите импортировать файл? Да/нет: ').lower()
    if command_import == 'да':
        data = Import.ImportFromFile()#надо прикрутить в метод указание пути, где лежит файл для импорта.
    while canWork:
        #try:
            command = input('Введите команлу: "Add" - чтобы добавить новый контакт, "Del" - чтобы удалить контакт, "Find" - чтобы найти контакт,  "Exit" - чтобы выйти из приложения. ')
            match command:
                case 'Add':
                    name = input('Введите имя: ')#реализовать метод проверки
                    #
                    #def input_check(data):
                    #if data.isdigit():
                    #    print('isdigit')
                    #elif data.isalpha():
                    #    print('isalpha')
                    #else:
                    #    print('Not digit or alpha')
                    #
                    surname = input('Введите фамилию: ')
                    phonenumber = input('Введите номер телефона: ')
                    Add.Add(name, surname, phonenumber)#Реализовать разбиение сплитом на список
                    print('Абонент сохранен в справочник.')
                case 'Read':
                    Read.ReadFhoneBook()
                case 'Del':
                    #Возможно стоит сделать только один метод на удаление, изменение и т.д.,
                    #т.к. мы все равно перед этим ищем пользователя?? Пока сделал так.
                    user = input('Кого Вы хотите удалить?')
                    if type(user) == int:
                        user_pool = list(Find.FindByPhoneNumber(user))
                        if len(user_pool)>1:
                            user_choice = input(int('Пользователя под каким номером Вы хотите удалить?'))
                            #Del.DeleteByPhoneNumber(user_pool[user_choice-1])
                        elif len(user_pool)==1:
                            Del.DeleteByPhoneNumber(user)
                    else:
                        user_pool = list(Find.FindByPhoneNumber(user))
                        Find.FindByName(user)
                        if len(user_pool)>1:
                            user_choice = input(int('Пользователя под каким номером Вы хотите удалить?'))
                            Del.DeleteByName(user_pool[user_choice-1])
                        elif len(user_pool)==1:
                            Del.DeleteByName(user_pool)

                case 'Edit':
                    user = input('Какой контакт Вы хотите изменить?')
                    Edit.EditByName(user)
                    Edit.EditByPhoneNumber(user)
                    Edit.EditBySurname(user)
                case 'Find':
                    user = input('Какой контакт Вы хотите найти?')

                    user_pool = list(Find.Find(user))# проверка на ввод и вызов нужного метода
                    if len(user_pool)>1:
                        user_choice = int(input('Пользователя под каким номером Вы хотите выбрать?'))
                        user_for_commands = user_pool[user_choice-1]
                        print(user_pool[user_choice-1])
                    elif len(user_pool)==1:
                        print(user_pool)
                        user_for_commands = user_pool
                    else:
                        print('Пользователи не найдены. ')
                    command_for_edit = input('Введите дальнейшую команду:\nEdit - для изменения контакта\nDel - для удаления контакта\nExit - для выхода вглавное меню.\n')
                    match command_for_edit:
                        case 'Edit':
                            123
                            #Нужно нарисовать команду Edit.
                        case 'Del':
                            Del.DeleteByName(user_for_commands)
                        case 'Exit':
                            break #? хз как это будет тут работать, надо потестить и сделать выход в меню.
                        case _:
                            print("Введены неправильные данные. Повторите ввод команды. ")
                    user_pool.clear()
                case 'Exit':
                    export = input('Хотите экспортировать файл телефонного справочника?\nДа/нет: ').lower()
                    if export == 'да':
                        Export.ExportContacts(data)
                    print('Завершение работы приложения...')
                    Exit.Exit(canWork)# а надо ли вообще отдельный метод, если можно просто присвоить тут False?
                case _:
                    print("Введены неправильные данные. Повторите ввод команды. ")
        #except:
        #    print("Введены неправильные данные. Перезапуск приложения...")

                




