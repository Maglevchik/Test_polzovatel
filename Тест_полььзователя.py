#Тест пользователя 10 вопросов по Пайтону
#Вывод по 1 вопросу
#Если ответ неверный, то еще раз задать пока не будет правильный, учитывать маленький большой регистр
#Статистика подсчета попыток, и вывод кол-ва правильных неправильных
#print(otvet[0])
#for word in otvet: print(word)
otvet = tuple(['Объект, возвращающий элементы по одному за раз','Текстовая информация','Возвращает количество элементов в объекте','utf-8','Python3','Условный','Бесконечный цикл','Перебирающий итератор','У него всегда определен конец итераций','in()'])
false_otvet = tuple(['Объект, возвращающий элементы по несколько за раз','Переменная','',''])

score_goodtry=0
score_badtry=0

a = True
aaa = True
print('Тест на знания Пайтона 10 вопросов')
while aaa == True:
    while a == True:
        print('1.Что такое Итерабельный объект(Iterable)?')
        print('    1){0}\n    2){1}\n    3){2}'.format(otvet[0],false_otvet[0],false_otvet[1]))
        otvet_input = str(input())
        if otvet_input == otvet[0]:
            print('Верный ответ.')
            a = False
            score_goodtry+=1
        elif otvet_input == false_otvet[0] or false_otvet[1]:
            print('Неверный ответ.')
            score_badtry += 1
            a = True
        else:
            print('Не понял')
            a = True

    a = True
    while a == True:
        print('2.Что такое Строки?')
        print('    1){0}\n    2)abc\n    3)bca'.format(otvet[1]))
        otvet_input = str(input()).lower()
        if otvet_input in otvet[1]:
            a = False
            score_goodtry+=1
        else:
            a = True
            score_badtry+=1

    a = True
    while a == True:
        print('3.Что делает функция len()?')
        print('    1){0}\n    2)abc\n    3)bca'.format(otvet[2]))
        otvet_input = str(input()).lower()
        if otvet_input in otvet[2]:
            a = False
            score_goodtry+=1
        else:
            a = True
            score_badtry+=1

    aaa = False
score_try= score_goodtry+score_badtry
print(score_try, score_badtry, score_goodtry)
print('Всего попыток: {0}, Плохие: {1}, Хорошие: {2}'.format(score_try,score_badtry,score_goodtry))

#print('1.Что такое Итерабельный объект(Iterable)?')
#print(otvet[0])
#print('2.Что такое Строки?')
#print(otvet[1])
#print('3.Что делает функция len()?')
#print(otvet[2])
print('4.Какая кодировка является стандартом для вывода текста?')
print(otvet[3])
print('5.Какая версия языка сейчас актуальна?')
print(otvet[4])
print('6.О каком операторе идет речь: Они позволяют программам принимать решения, изменять ход выполнения в зависимости от заданных условий?')
print(otvet[5])
print('7.Что присуще циклу "while" чего нет у "for"?')
print(otvet[6])
print('8.Как называют по-умному цикл "for"?')
print(otvet[7])
print('9.Какая специфика цикла "for"?')
print(otvet[8])
print('10.Какой оператор помогает вычислить принадлежность или присутствие символов в строке')
print(otvet[9])