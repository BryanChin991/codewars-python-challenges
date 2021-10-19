def duplicate_count(text):
    d={}
    count = 0
    for i in text.lower():
        d[i] = d.get(i, 0) + 1
    for i in d.values():
        if i > 1:
            count+=1
    print(count)

    # occurred = []
    # count = 0
    #
    # [occurred.append(letter) if letter not in occurred else None for letter in text.lower()]
    # print(occurred)



duplicate_count('Indivisibilities')
duplicate_count('abcdeaB')
