from datetime import datetime

def Add_logger(data):
    time = datetime.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{time} added {data}.\n')
    file.close()

def Del_logger(data):
    time = datetime.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{time} deleted {data}.\n')
    file.close()

def Edit_logger(data):
    time = datetime.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{time} edited {data}.\n')
    file.close()




