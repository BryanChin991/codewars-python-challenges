from collections import Counter

def arrayManipulation(n, queries):
    c = Counter()
    for a,b,k in queries:
        c[a] += k
        c[b+1] -= k

    arrSum = 0
    maxSum = 0
    print(f'sorted(c): {sorted(c)}, c: {c}, sorted(c)[:-1]: {sorted(c)[:-1]}')
    for i in sorted(c)[:-1]:
        arrSum += c[i]
        maxSum = max(maxSum, arrSum)
        print(i, arrSum)
    print(maxSum)

arrayManipulation(5, [[1, 2, 100],
                      [2, 5, 100],
                      [3, 4, 100]])

arrayManipulation(10, [[2, 6, 8],
                       [3, 5, 7],
                       [1, 8, 1],
                       [5, 9, 15]])