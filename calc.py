c = input("Введите математическое вычисление(+,-,*,/): ")
if c not in ('+', '-', '*', '/'):
 print('Неверный символ')
 quit()


a = float(input('Введите число 1: a= '))
b = float(input('Введите число 2: b= '))

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == "*":
    print(a * b)
if b==0:
 print('Деление на 0')
elif c == "/":
    print(a / b)

print("Тип данных в a:", type(a))
print("Тип данных в b:", type(b))
print("Тип данных в c:", type(c))
