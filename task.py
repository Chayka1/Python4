def task_1_1():
    name = open('files/my_name.txt', 'w')
    name.write('Max')
    name.close()

def task_2_2():
    name = open('files/my_name.txt', 'r')
    for name_ in name:
        print(name_)
    name.close()

