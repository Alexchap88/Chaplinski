import ru as ru
from num2words import num2words

counter = 0
while True:

    try:
        a = float(input('Введите число :  '))
    except ValueError as e:
        print(e)

    c = input("Введите математическое вычисление(+,-,*,/): ")
    if c not in ('+', '-', '*', '/'):
        print('Неверный символ')
        quit()
    try:
        b = float(input('Введите число :  '))
    except ValueError as h:
        print(h)

    counter += 1
    print('Результат', counter)

    if c == '+':
        print(num2words(a + b, lang='ru'))

    elif c == '-':
        print(num2words(a - b, lang='ru'))
    elif c == "*":
        print(num2words(a * b, lang='ru'))
    if b == 0:
        print('Деление на 0')
    elif c == "/":
        print(num2words(a / b, lang='ru'))

    d = input("Введите 'стоп' для выхода из программы либо любой символ для продолженя: ")
    if d in ('стоп'):
        break
    continue




