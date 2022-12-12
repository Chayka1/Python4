def task_1_1():
    name = open('files/my_name.txt', 'w')
    name.write('Max')
    name.close()


def task_1_2():
    name = open('files/my_name.txt', 'r')

    for name_ in name:
        print(name_)

    name.close()


def task_1_3():
    nums = open('files/number_list.txt', 'w')

    for nums_ in range(1, 101):
        nums.write(str(nums_))
        nums.write('\n')

    nums.close()


def task_1_4():
    nums = open('files/number_list.txt', 'r')

    for nums_ in nums:
        nums_ = nums_.rstrip('\n')
        print(nums_)

    nums.close()


def task_1_5():
    total = 0

    nums = open('files/number_list.txt', 'r')

    for nums_ in nums:
        nums_ = nums_.rstrip('\n')
        nums_ = int(nums_)
        total += nums_

    print(total)

    nums.close()

def task_1_6():
    nums = open('files/number_list.txt', 'r')
    nums.close()

def task_1_7():
    students = open('files/students.txt', 'r')

    for names in students:
        names = names.rstrip('\n')
        names = names.replace('Джон Перц 70', '')

    students.close()

def task_1_8():
    students = open('files/students.txt', 'r')

    for names in students:
        names = names.rstrip('\n')
        names = names.replace('Джулия Милан 70', 'Джулия Милан 100')

    students.close()

