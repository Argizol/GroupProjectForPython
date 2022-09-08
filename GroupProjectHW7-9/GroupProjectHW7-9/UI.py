import AddCommand as Add
import DeleteCommand as Del
import EditCommand as Edit
import ExitCommand as Exit
import FindCommands as Find
import logger as log

def Menu():
    canWork = True
    while canWork:
        try:
            command = input('Добро пожаловать в телефонный справочник.\n Введите команду: ')
            match command:
                case 'Add':
                    name = input('Введите имя: ')
                    surname = input('Введите фамилию: ')
                    phonenumber = input('Введите номер телефона: ')
                    Add.Add(name, surname, phonenumber)
                    print('Абонент сохранен в справочник.')
                    log.Add_logger(Add.Add) #тут не уверен в правильности написания, мб надо сделать сохранение data в переменную?
                case 'Del':
                    user = input('Кого Вы хотите удалить?')
                    Del.DeleteByName(user)
                    Del.DeleteByPhoneNumber(user)
                    Del.DeleteBySurname(user)
                case 'Edit':
                    user = input('Какой контакт Вы хотите изменить?')
                    Edit.EditByName(user)
                    Edit.EditByPhoneNumber(user)
                    Edit.EditBySurname(user)
                case 'Find':
                    user = input('Какой контакт Вы хотите найти?')
                    Find.FindByName(user)
                    Find.FindByPhoneNumber(user)
                    Find.FindBySurname(user)
                case 'Exit':
                    print('Завершение работы приложения...')
                    Exit.Exit(canWork)
                case _:
                    print("Введены неправильные данные. Повторите ввод команды. ")
        except:
            print("Введены неправильные данные. Перезапуск приложения...")

                




