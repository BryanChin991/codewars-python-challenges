'''def high(x):
    x = x.lower()
    x = x.split()
    d = {}
    for word in x:
        sum = 0
        for letter in word:
            sum += (ord(letter) - 96)
        d[word] = sum
    li = list(d.items())
    li.sort(key=lambda x: x[1], reverse=True)
    return li[0][0]'''

def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


high('man i need a taxi up to ubud')
high('what time are we climbing up the volcano')
high('aa b')
high('b aa')