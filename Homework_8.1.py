def add_one(some_list):
    one = 1
    ind = len(some_list) - 1
    while ind >= 0:
        dig = some_list[ind] + one
        if dig < 10:
            some_list[ind] = dig
            one = 0
            break
        else:
            some_list[ind] = 0
            one = 1
        ind -= 1
    if one:
        some_list.insert(0, 1)
    return some_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1' 
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2' 
assert add_one([0]) == [1], 'Test3' 
assert add_one([9]) == [1, 0], 'Test4' 
print("ОК")
