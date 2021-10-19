def spin_words(words):
    # words = words.split()
    # li=[]
    # for w in words:
    #     if len(w) > 4:
    #         w[::-1]
    #     li.append(w)
    words = [w[::-1] if len(w)>4 else w for w in words.split()]
    print(' '.join(words))
    return ' '.join(words)

spin_words('Welcome')
spin_words('This is another test ')
spin_words('Hey fellow warriors')