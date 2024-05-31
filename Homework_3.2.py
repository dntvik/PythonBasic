lst = [12, 3, 4, 10, 8]
if len(lst) <= 1:
    lst = lst
else:
    print(lst)
    x = lst[-1]
    lst = lst[:-1]
    lst.insert(0, x)
print(lst)
