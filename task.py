def task_1_1():
    name = open('my_name.txt', 'w')
    name.write('Max')
    name.close()


def task_1_2():
    name = open('my_name.txt', 'r')

    for name_ in name:
        print(name_)

    name.close()


def task_1_3():
    nums = open('number_list.txt', 'w')

    for nums_ in range(1, 101):
        nums.write(str(nums_))
        nums.write('\n')

    nums.close()


def task_1_4():
    nums = open('number_list.txt', 'r')

    for nums_ in nums:
        nums_ = nums_.rstrip('\n')
        print(nums_)

    nums.close()


def task_1_5():
    total = 0

    nums = open('number_list.txt', 'r')

    for nums_ in nums:
        nums_ = nums_.rstrip('\n')
        nums_ = int(nums_)
        total += nums_

    print(total)

    nums.close()


def task_1_6():
    nums = open('number_list.txt', 'r')
    nums.close()


def task_1_7():
    students = open('students.txt', 'r')

    for names in students:
        names = names.rstrip('\n')
        names = names.replace('Джон Перц 70', '')

    students.close()


def task_1_8():
    students = open('students.txt', 'r')

    for names in students:
        names = names.rstrip('\n')
        names = names.replace('Джулия Милан 70', 'Джулия Милан 100')

    students.close()


def task_1_9():
    try:
        x = float('abc123')
        print('Конвертация завершена')
    except IOError:
        print('Этот программный код вызвыл ошибку I0Error')
    except ValueError:
        print('Этот программный код вызвыл ошибку ValueError')
    print('Конец')


def task_1_10():
    try:
        x = float('abc123')
        print('Конвертация завершена')
    except IOError:
        print('Этот программный код вызвыл ошибку I0Error')
    except ZeroDivisionError:
        print('Этот программный код вызвыл ошибку ZeroDivisionError')
    except:
        print('Произошла ошибка')
    print('Конец')


def task_2_1():
    nums = open('numbers.txt', 'r')

    for nums_ in nums:
        print(nums_)

    nums.close()


def task_2_2():
    filename = input('Введите имя файла: ')

    f = open(filename, 'r')

    line_count = sum(1 for line in open(filename))
    if line_count < 5:
        for i in range(line_count):
            print(f.readline())
    else:
        for i in range(5):
            print(f.readline())

    f.close()


def taks_2_3():
    filename = input('Введите имя файла: ')

    f = open(filename, 'r')

    numbers = 0
    for lines in f:
        numbers += 1
        lines = lines.rstrip('\n')
        print(f'{numbers}: {lines}')


def task_2_4():
    f = open('names.txt', 'r')

    total = 0
    for line in f:
        total += 1

    print(total)


def task_2_5():
    f = open('nums.txt', 'r')

    total = 0

    for num in f:
        num = int(num)
        total += num

    print(total)

