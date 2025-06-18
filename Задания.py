numbers = [1, 2, 3, 4, 5]
def task1_1():
    numbers.append(6)
    numbers.insert(0, 0)
    numbers.remove(3)
    print(f'\nСоздание и модификация списков{numbers}')

def task1_2():
    print(f'\nПолучите первые три элемента списка.{numbers[0:3]}'
          f'\nПолучите все элементы с третьего до конца списка.{numbers[0:3]}'
          f'\nПолучите каждый второй элемент списка.{numbers[::2]}'
          f'\nРазверните список.{numbers[::-1]}')

def task1_3(x=None):
    squares = [x**2 for x in range(11) if x % 2 == 0]
    print(f'\nКвадраты четных чисел от 1 до 10.{squares}')

def task2_1():
    student = {"name": None, 'age': None, 'grade' : None}
    student['subject'] = 'Python'
    student['grade'] = '18'
    del student['age']
    print(f'\nСоздание и модификация словарей.{student}')

def task2_2():
    square_dict = {}
    for i in range(1, 6):
        square_dict[i] = i**2
    print(f'\nDict Comprehension.{square_dict}')

def task3():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f'\nСоздайте объединение множеств.{set1 | set2}'
          f'\nНайдите пересечение множеств.{set1 & set2}'
          f'\nНайдите разность множеств.{set1 & set2}')

def fibonacci_dict(n):
    fib_dict = {}
    fib_sequence = [0, 1]

    if not isinstance(n, int) or n < 0:
        print("Входное значение 'n' должно быть неотрицательным целым числом.")

        # Инициализируем словарь для 0 и 1
    if n >= 0:
        fib_dict[0] = [0]
    if n >= 1:
        fib_dict[1] = [0, 1]

        # Генерируем последовательность Фибоначчи и заполняем словарь
    for i in range(2, n + 1):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

        # Обновляем значения для каждого ключа
    current_fib_list = []
    for fib_num in fib_sequence:
        if fib_num <= i:
            current_fib_list.append(fib_num)
        else:
            break  # Если число Фибоначчи превышает ключ, дальше проверять нет смысла
    fib_dict[i] = current_fib_list

    print(f'\nЧисло Фибоначчи.{fib_dict}')


task1_1()
task1_2()
task1_3()
task2_1()
task2_2()
task3()
fibonacci_dict(5)
