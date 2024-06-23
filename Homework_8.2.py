import string


def is_palindrome(text):
    text = text.lower()
    text2 = []
    for i in text:
        if i in string.ascii_lowercase or i in string.digits:
            text2.append(i)
    text2 = ''.join(text2)
    return text2 == text2[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') is True, 'Test1'
assert is_palindrome('0P') is False, 'Test2'
assert is_palindrome('a.') is True, 'Test3'
assert is_palindrome('aurora') is False, 'Test4'
print("ОК")
