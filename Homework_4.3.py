import random

quantity = random.randint(3, 10)
lst = [random.randint(0, 100) for i in range(quantity)]
new = [lst[0], lst[2], lst[-2]]
print(lst, '==', new)
