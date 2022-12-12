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

