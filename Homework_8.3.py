def find_unique_value(some_list):
    dict1 = {}
    for i in some_list:
        dict1.setdefault(i, 0)
        dict1[i] += 1
    for i in some_list:
        if dict1[i] == 1:
            return i


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
