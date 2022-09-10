from Contacts import data
import logger as Log

def DeleteByName(name):
     for j, k in data.items():
        if j.__contains__(name):
            del data[j]
            Log.Del_logger(f'{j} {k}')


def DeleteByPhoneNumber(phoneNum):
    for j, k in data.items():
        if k.__contains__(phoneNum):
            del data[j]
            Log.Del_logger(f'{j} {k}')




