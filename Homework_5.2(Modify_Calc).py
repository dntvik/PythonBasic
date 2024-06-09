while True:
    num1 = float((input('Введіть перше число: ')))
    num2 = float((input('Введіть друге число: ')))
    oper = input('Введіть запропонований математичний оператор(+, - , *, /): ')
    if oper == '/' and num2 == 0:
        print('На нуль ділити не можна')
    else:
        if oper == '+':
            res = num1 + num2
        elif oper == '-':
            res = num1 - num2
        elif oper == '*':
            res = num1 * num2
        elif oper == '/' and num2 != 0:
            res = num1 / num2
        else:
            res = None
            print('Помилка')
        if res is not None:
            if res % 1 == 0:
                print(int(res))
            else:
                print(res)
    i = input('Бажаєте зробити ще одне обчислення (y/n)?: ')
    if i != 'yes' and i != 'y':
        break
