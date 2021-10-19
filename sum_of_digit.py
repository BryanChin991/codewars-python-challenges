def digital_root(n):
    if n < 0:
        return -1
    elif n < 10:
        return n
    else:
        s = (n % 10) + digital_root(int(n/10))
        if s < 10:
            return s
        else:
            return (s % 10) + digital_root(int(s/10))


inp = input('x: ')
print(digital_root(int(inp)))