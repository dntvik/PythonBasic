def second_index(text, some_str):
    f_ind = text.find(some_str)
    if f_ind == -1:
        return None
    s_ind = text.find(some_str, f_ind + 1)
    if s_ind == -1:
        return None
    return s_ind


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
