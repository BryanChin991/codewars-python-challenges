'''import numpy as np
def valid_solution(board):
    d, d2, d3 = {}, {}, {}

    for idx, i in enumerate(range(0, 9, 1), start=1):
        for j in board[i]:
            d[j] = d.get(j, 0) + 1
        # print(d)
        for key, val in d.items():
            if val != idx:
                return False
        for j in np.transpose(board)[i]:
            d3[j] = d3.get(j, 0) + 1
        # print(d)
        for key, val in d3.items():
            if val != idx:
                return False

    for i in board[:3]:
        for j in i[:3]:
            d2[j] = d2.get(j, 0) + 1
        for key, val in d2.items():
            if val != 1:
                return False
    return True'''

# PEP 8 - Function names should be in snake_case
def valid_solution(m):
    is_valid = lambda a: len(a) == 9 and all([i + 1 in a for i in range(9)])
    get_block_as_row = lambda n: [m[3 * (n / 3) + (i / 3)][(3 * n) % 9 + i % 3] for i in range(9)]
    return all([is_valid(r) for r in m]) and all([is_valid([r[i] for r in m]) for i in range(9)]) and all([is_valid(get_block_as_row(i)) for i in range(9)])

# Just to pass the Kata
validSolution = valid_solution



# valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
#                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
#                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
#                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
#                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
#                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                    [3, 4, 5, 2, 8, 6, 1, 7, 9]])
#
# valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
#                    [6, 7, 2, 1, 9, 0, 3, 4, 9],
#                    [1, 0, 0, 3, 4, 2, 5, 6, 0],
#                    [8, 5, 9, 7, 6, 1, 0, 2, 0],
#                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                    [9, 0, 1, 5, 3, 7, 2, 1, 4],
#                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                    [3, 0, 0, 4, 8, 1, 1, 7, 9]])
#
# valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9],
#                 [2, 3, 4, 5, 6, 7, 8, 9, 1],
#                 [3, 4, 5, 6, 7, 8, 9, 1, 2],
#                 [4, 5, 6, 7, 8, 9, 1, 2, 3],
#                 [5, 6, 7, 8, 9, 1, 2, 3, 4],
#                 [6, 7, 8, 9, 1, 2, 3, 4, 5],
#                 [7, 8, 9, 1, 2, 3, 4, 5, 6],
#                 [8, 9, 1, 2, 3, 4, 5, 6, 7],
#                 [9, 1, 2, 3, 4, 5, 6, 7, 8]])

valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                [4, 9, 8, 2, 6, 1, 3, 7, 5],
                [7, 5, 6, 3, 8, 4, 2, 1, 9],
                [6, 4, 3, 1, 5, 8, 7, 9, 2],
                [5, 2, 1, 7, 9, 3, 8, 4, 6],
                [9, 8, 7, 4, 2, 6, 5, 3, 1],
                [2, 1, 4, 9, 3, 5, 6, 8, 7],
                [3, 6, 5, 8, 1, 7, 9, 2, 4],
                [8, 7, 9, 6, 4, 2, 1, 3, 5]])

