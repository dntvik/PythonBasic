input_sec = int(input('Введіть кількість секунд, від 0 до 8640000:\n'))
if not 0 <= input_sec <= 8640000:
    print('Уважно прочитай, який діапазон секунд тобі дозволений!')
else:
    cont_minutes, sec = divmod(input_sec, 60)
    cont_hours, minutes = divmod(cont_minutes, 60)
    days, hours = divmod(cont_hours, 24)
    days_name = {1: 'День', 2: 'Дні', 3: 'Днів'}
    days_name_true = 0
    if days % 10 == 1:
        days_name_true = days_name[1]
    if 2 <= days % 10 <= 4:
        days_name_true = days_name[2]
    if days % 10 >= 5 or days % 10 == 0 or 11 <= days <= 19:
        days_name_true = days_name[3]
    time = str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(sec).zfill(2)
    print(str(input_sec) + ' -> ' + str(days), days_name_true + ',', time)
