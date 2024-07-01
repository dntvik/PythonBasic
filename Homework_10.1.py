def pow(x):
    return x ** 2


def some_gen(begin, end, func):
    result = begin
    for i in range(end):
        yield result
        result = func(result)


from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) is True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
