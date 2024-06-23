def popular_words(text, words):
    dict1 = {}
    text = text.lower()
    text = text.split()
    for i in words:
        dict1[i] = text.count(i)
    for i in words:
        if i not in dict1:
            dict1[i] = 0

    return dict1


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
