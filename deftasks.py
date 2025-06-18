print('\nЗадача 1. Вычисление площади прямоугольника')
length = int(input('length: '))
width = int(input('width: '))
def calculate_area(length,width):
    print(f'Площадь прямоугольника с длиной {length} и шириной {width}: {length * width}')
calculate_area(length,width)

print('\nЗадача 2. Проверка четности числа')
num = int(input('Четное, нечетное: '))
def is_even(number):
    if number % 2 == 0:
        print(True)
    else:
        print(False)
is_even(num)

print('\nЗадача 3. Увеличение счетчика')
step = int(input('Шаг: '))
counter = 1
def increment_counter(step):
    global counter
    if step == None:
        counter += 1
    else:
        counter += step
    print(counter)
increment_counter(step)

print('\nЗадача 4. Расчет цены со скидкой')
original_price = int(input('ориг цена: '))
discount_percentage = int(input('Скидка на товар % : '))
def calculate_discounted_price(original_price, discount_percentage):
    # Lambda-функция для вычисления суммы скидки
    calculate_discount_amount = lambda price, discount: price * (discount / 100)

    discount_amount = calculate_discount_amount(original_price, discount_percentage)
    discounted_price = original_price - discount_amount
    print(f'Цена с примененной скидкой: {discounted_price}')
calculate_discounted_price(original_price, discount_percentage)

print('\nЗадача 5. Программа для выбора математической операции')
def add(x, y):
    """Возвращает сумму двух чисел."""
    return x + y
def subtract(x, y):
    """Возвращает разность двух чисел."""
    return x - y
def multiply(x, y):
    """Возвращает произведение двух чисел."""
    return x * y
def divide(x, y):
    """Возвращает частное двух чисел, обрабатывая деление на ноль."""
    if y == 0:
        return "Ошибка: Деление на ноль невозможно."
    return x / y

def calculator():
    """
    Позволяет пользователю выбирать математические операции и выполняет их.
    """
    print("Выберите операцию:"
          "1. Сложение"
          "2. Вычитание"
          "3. Умножение"
          "4. Деление")

    while True:
        choice = input("Введите номер операции (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите числа.")
                continue

            if choice == '1':
                print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")

            break  # Выходим из цикла после успешной операции
        else:
            print("Неверный выбор. Пожалуйста, введите номер от 1 до 4.")

# Запуск программы
calculator()