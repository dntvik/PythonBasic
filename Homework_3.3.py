lst = [1, 2, 3, 4, 5]
lenl = len(lst)
mid = (len(lst)+1)//2
lst1 = lst[:mid]
lst2 = lst[mid:]
lst3 = [lst1, lst2]
if lenl == 0:
    lst.append([])
    lst *= 2
    print(lst)
else:
    print(lst3)
