from Contacts import data
import logger as Log

def Delete(user_data):
    global data
    for j, k in data.copy().items():
        if k == user_data:
            del data[j]
            Log.Del_logger(f'{j} {k}')


#def DeleteByPhoneNumber(phoneNum):
#    for j, k in data.items():
#        if k.__contains__(phoneNum):
#            del data[j]
#            Log.Del_logger(f'{j} {k}')




