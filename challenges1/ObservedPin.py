pin = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [None, 0, None]]

def adjancent(n):
    length = len(n)
    for idx, p_row in enumerate(pin):
        for idy, p_col in enumerate(p_row):
            if int(n) == p_col:
                # return print(idx, idy, len(pin), len(p_row))
                # if idx-1 >= 0 and idx < len(pin) and idy-1 >=0 and idy < len(p_row):
                return print(list(
                                    { pin[idx-1 if idx-1 >=0 else 0][idy],
                                      pin[idx][idy-1 if idy-1 >=0 else 0],
                                      str(pin[idx][idy]) * length,
                                      pin[idx][idy+1 if idy+1 < len(p_row) else len(p_row)-1],
                                      pin[idx+1 if idx+1 < len(pin) else len(pin)-1][idy]}))
adjancent('77')
