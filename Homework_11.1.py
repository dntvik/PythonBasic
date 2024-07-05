def prime_generator(n):
    A = [True] * (n + 1)
    A[0], A[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if A[i]:
            for j in range(i * i, n + 1, i):
                A[j] = False
    for i in range(2, n + 1):
        if A[i]:
            yield i


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
