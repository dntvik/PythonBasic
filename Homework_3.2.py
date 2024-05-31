lst = [1,2,3,4,5]
if len(lst) <= 1:
    lst = lst
else:
    print(lst)
    x = lst[-1]
    lst = lst[:-1]
    lst.insert(0, x)
print(lst)
