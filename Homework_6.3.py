num = input('Введіть ціле число:\n')
result = num
while len(num) > 1:
    result = 1
    for i in list(num):
        result *= int(i)
    num = str(result)
print(result)
