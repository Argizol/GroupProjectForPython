import datetime as dt

def Add_logger(data):
    time = dt.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{time} added {data}.')
        file.write(' ')
    file.close()

def Del_logger(data):
    time = dt.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{time} deleted {data}.')
        file.write(' ')
    file.close()

def Edit_logger(data):
    time = dt.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{time} edited {data}.')
        file.write(' ')
    file.close()




