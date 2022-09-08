from Contacts import data

def FindByName(name, data):
     for j, k in data.items():
        if j.__contains__(name):
            print(j, k, sep=', ')

def FindByPhoneNumber(phoneNum):
     for j, k in data.items():
        if k.__contains__(phoneNum):
            print(j, k, sep=', ')


