lst = [1, 2, 3]
if len(lst) > 1:
    x = lst.pop()
    lst.insert(0, x)
else:
    lst = lst
print(lst)
