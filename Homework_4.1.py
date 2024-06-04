lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
for i in lst:
    zero_index = lst.index(0)
    zero_delete = lst.pop(zero_index)
    lst.extend([zero_delete])
print(lst)
