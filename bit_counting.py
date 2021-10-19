'''def count_bits(n):
    return sum([int(i) for i in bin(n) if i == '1'])'''

def count_bits(n):
    return bin(n).count("1")

print(count_bits(1234))
print(count_bits(0))
print(count_bits(4))
print(count_bits(7))
print(count_bits(9))
print(count_bits(10))