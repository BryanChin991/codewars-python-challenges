# using set {}
'''def sum_of_intervals(intervals):
    d = {}
    for idx, (f, l) in enumerate(intervals):
        d[idx] = {i for i in range(f+1, l+1, 1)}

    try:
        for i in range(len(intervals)):
            d[i+1] = d[i+1].union(d[i])
    except: pass

    # print(d[len(intervals)-1])
    return len(d[len(intervals)-1])'''

def sum_of_intervals(intervals):
    return len(set([n for (a, b) in intervals for n in [i for i in range(a, b)]]))

sum_of_intervals([
   [1,2],
   [6, 10],
   [11, 15]
])

sum_of_intervals([
    [1, 4],
    [7, 10],
    [3, 5]
])

sum_of_intervals([
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11]
])
