'''def next_bigger(n, length=5):
    s = list(map(int, str(n)))[::-1]
    # print(s[::-1], length)
    for i in range(length):
        for j in range(i, len(s)):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]
                print(int(''.join(map(str, s[:j-1:-1]+ s[:j]))))
                return int(''.join(map(str, s[:j-1:-1]+ s[:j])))'''

def next_bigger(n):
    s = list(map(int, str(n)))[::-1]
    # print(s[::-1], length)
    for i in range(len(s)):
        if i + 1 < len(s):
            if s[i] > s[i+1]:
                num = i+1
                for j in range(len(s)):
                    if s[j]>s[num]:
                        num2 = j
                        break
                # return print(num, num2)
                s[num], s[num2] = s[num2], s[num]
                print(''.join(map(str, s[:i:-1] + s[:i+1])))
                return int(''.join(map(str, s[:i:-1] + s[:i+1])))


# next_bigger(12)         # 21
# next_bigger(513)        # 531
# next_bigger(2017)       # 2071
# next_bigger(414)        # 441
# next_bigger(144)        # 414
next_bigger(1318540)       # 1340158
next_bigger(961541811572)       # 961541811725