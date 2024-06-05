lst = [0, 1, 7, 2, 4, 8]
if len(lst) == 0:
    result = 0
else:
    summa = 0
    for i in range(0, len(lst), 2):
        summa += lst[i]
    result = summa * lst[-1]
print(result)
