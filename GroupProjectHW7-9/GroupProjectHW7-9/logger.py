def Add_logger(data):
    time = dt.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{dt} added {data}.')
        file.write(' ')
    file.close()

def Del_logger(data):
    time = dt.now().strftime('%H:%M')
    with open("log.csv", "a") as file:
        file.write(f'{dt} deleted {data}.')
        file.write(' ')
    file.close()




