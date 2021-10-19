def order(sentence):
    d = {}
    words = sentence.split()
    for word in words:
        for letter in word:
            if letter.isnumeric():
                d[int(letter)] = word
    li = list(d.items())
    li.sort()
    res = []
    for num, word in li:
        res.append(word)

    return ' '.join(res)

order('is2 Thi1s T4est 3a')
print(order('4of Fo1r pe6ople g3ood th5e the2'))
order('')