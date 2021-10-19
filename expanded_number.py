'''def expanded_form(num):
    li = []
    for i, n in enumerate(str(num)):
        if n != '0':
            li.append(str(10**(len(str(num)) - i - 1) * int(n)))
    return ' + '.join(li)'''

def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

expanded_form(12)
expanded_form(42)
expanded_form(70304)