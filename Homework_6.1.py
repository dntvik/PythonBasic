import string

inp_let = input('Введіть діапазон букв: перша_буква-друга_буква. Приклад: a-x:\n')
let = string.ascii_letters
lett = inp_let.split('-')
first = lett[0]
last = lett[1]
first_ind, last_ind = let.index(first), let.index(last) + 1
result = let[first_ind:last_ind]
print(result)
