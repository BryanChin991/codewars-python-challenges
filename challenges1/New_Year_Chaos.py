def minimumBribes(q):
    count, temp = 0, 0
    c = q.copy()
    c.sort()
    for i, j in zip(q, c):
        if i - j > 2:
            print('Too chaotic')
            return
    while q != c:
        for i in range(len(q)):
            if i == len(q) - 1: continue
            if q[i] > q[i + 1]:
                temp = q[i]
                q[i] = q[i + 1]
                q[i + 1] = temp
                count += 1
    print(count)

minimumBribes([2, 1, 5, 3, 4])
minimumBribes([2, 5, 1, 3, 4])
minimumBribes([7, 1, 3, 2, 4, 5, 6])


4, 3, 1, 2
3, 4, 1, 2
