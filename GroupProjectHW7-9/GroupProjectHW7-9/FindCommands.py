from Contacts import data
def Find(user_data):
    global data
    list1 = []
    for j, k in data.items():
       if (user_data in j) or (user_data in k):
            list1.append(f'{j}, {k}')
    for idx, el in enumerate(list1):
        print(idx+1, el)
    return list1

