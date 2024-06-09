import string

input_hash = input('Введіть текст не більше 140 символів: ')
cl = ''
for i in input_hash:
    if i not in string.punctuation:
        cl += i
title_hash = cl.title().replace(' ', '')
res_hash = '#' + title_hash
if len(res_hash) > 140:
    res_hash = res_hash[:140]
print(res_hash)
