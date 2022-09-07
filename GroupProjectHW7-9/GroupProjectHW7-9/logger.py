def add_logger(data):
    time = dt.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{dt} added {data}.')
        file.write(' ')
    file.close()

def del_logger(data):
    time = dt.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{dt} deleted {data}.')
        file.write(' ')
    file.close()




