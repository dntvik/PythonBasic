import keyword
import string

name = input("Введіть ім'я змінної: ")
if len(name) == 0 or name[0] in string.digits or ' ' in name:
    x = False
else:
    x = True
    underscore_count = 0
    for i in name:
        if i.isupper():
            x = False
            break
        if i in string.punctuation and i != '_':
            x = False
            break
        if i == '_':
            underscore_count += 1
    if 1 < underscore_count == len(name):
        x = False
    if name in keyword.kwlist:
        x = False
print(x)
