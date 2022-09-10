from Contacts import data

def FindByName(name, data):
     count = 1
     for j, k in data.items():
        if j.__contains__(name):
            print(count, j, k, sep=', ')
            count+= 1;
        else:
            print('Пользователей с таким именем не существует.')

def FindByPhoneNumber(phoneNum):
     count = 1
     for j, k in data.items():
        if k.__contains__(phoneNum):
            print(count, j, k, sep=', ')
            count+= 1
        else:
            print('Пользователей с таким номером не существует.')


