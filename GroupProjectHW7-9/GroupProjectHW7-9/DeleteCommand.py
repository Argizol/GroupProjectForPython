from Contacts import data
def DeleteByName(name):
     for j, k in data.items():
        if j.__contains__(name):
            del data[j]


def DeleteByPhoneNumber(phoneNum):
    for j, k in data.items():
        if k.__contains__(phoneNum):
            del data[j]




