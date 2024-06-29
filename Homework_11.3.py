def is_even(digit):
    return (digit & 1) == 0


assert is_even(2) is True, 'Test1'
assert is_even(5) is False, 'Test2'
assert is_even(0) is True, 'Test3'
print('OK')
