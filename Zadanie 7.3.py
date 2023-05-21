a = int(input('Введите число '))
while a == 7:
    print('Good bye!')
    break
else:
    if a < 0:
        print('Number is negative ')
    elif a > 0:
        print('Number is positive')
    elif a == 0:
        print('Number is equal to zero')