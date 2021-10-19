'''def iq_test(numbers):
    d = {}
    for i, num in enumerate(numbers.split(' '), start=1):
        d[i] = int(num)%2

    for key, val in d.items():
        if sum(d.values()) == 1 and val == 1:
                return key
        elif sum(d.values()) > 1 and val == 0:
                return key'''

def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 1 1"))