import random
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

    f.close()


def task_2_4():
    f = open('names.txt', 'r')

    total = 0
    for line in f:
        total += 1

    print(total)

    f.close()


def task_2_5():
    f = open('nums.txt', 'r')

    total = 0

    for num in f:
        num = int(num)
        total += num

    print(total)

    f.close()


def task_2_6():
    f = open('nums.txt', 'r')

    total = 0
    amount = sum(1 for line in open('nums.txt'))

    for num in f:
        num = int(num)
        total += num

    average = total / amount

    print(f'Среднее арифметическое равно: {average}')

    f.close()


def task_2_7():
    amount = int(input('Введите количество рандомных чисел: '))
    file = open('random_numbers.txt', 'w')

    for i in range(amount):
        nums = random.randint(1, 500)
        file.write(f'{nums}\n')

    file.close()


def task_2_8():
    total = 0
    with open("random_numbers.txt") as f:
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in lines]
    random_line = random.choices(lines, k=random.randrange(len(lines)))

    amount_of_numbers = len(random_line)

    for num in random_line:
        total += int(num)

    print(f'Рандомные числа: {random_line}\n'
          f'Количество чисел: {amount_of_numbers}\n'
          f'Сумма чисел: {total}')


def task_2_9():
    global amount, f
    total = 0
    try:
        f = open('nums.txt', 'r')
        amount = sum(1 for line in open('nums.txt'))

        for num in f:
            num = int(num)
            total += num
    except IOError:
        print(IOError)
    except ValueError:
        print(ValueError)
    finally:
        average = total / amount

        print(f'Среднее арифметическое равно: {average}')

        f.close()


def task_2_10():
    def program1():
        f = open('golf.txt', 'w')

        action = 'да'

        while action == 'да':
            name = input('Введите имя: ')
            points = input('Введите очки: ')

            f.write(name + '\n')
            f.write(points + ' очков\n')

            action = input('Хотите ещё добавить игрока да/нет? ')
        else:
            f.close()

    program1()

    def program2():
        f = open('golf.txt', 'r')

        for players in f:
            players = players.rstrip('\n')
            print(players)

        f.close()

    program2()


def task_2_11():
    f = open('index.html', 'w')

    name = input('Введите имя: ')
    description = input('Опишите себя: ')
    indexHtml = f'<html>\n' \
                f'<head>\n' \
                f'</head>\n' \
                f'<body>\n' \
                f' <center>\n' \
                f' <h1>{name}<h1>\n' \
                f' <center>\n' \
                f' <hr />\n' \
                f' {description}\n' \
                f' <hr />\n' \
                f'</body>\n' \
                f'</html>'

    f.write(indexHtml)
    f.close()


