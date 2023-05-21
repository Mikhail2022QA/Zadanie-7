a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
while (a == 7 or b == 7):
    print('Good bye!')
    break
else:
    if a > b:
        print('Максимальное число ',a, 'сумма ', a+b)
    elif b > a:
        print('Максимальное число ',b, 'сумма ', a+b)
    elif b == a:
        print('Числа равны ' , b, 'сумма ', a+b)