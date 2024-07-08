import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    cl_tx = []
    _text = False

    for i in html:
        if i == '<':
            _text = True
        elif i == '>':
            _text = False
        elif not _text:
            cl_tx.append(i)

    cl_tx = ''.join(cl_tx)
    cl_tx = [line.strip() for line in cl_tx.splitlines() if line.strip()]
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(cl_tx))


delete_html_tags('draft.html')
