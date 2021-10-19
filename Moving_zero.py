'''def move_zeros(array):
    li = []
    count = 0
    for num in array:
        if num == 0:
            count += 1
            li.append(count)
        else:
            li.append(count)

    for i in range(len(array)):
        if array[i] != 0:
            array[i - li[i]] = array[i]
        if i >= len(array) - li[-1]:
            array[i] = 0

    return array'''
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros([0, 0, 2, 1]))
print(move_zeros([0]))