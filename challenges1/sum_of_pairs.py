def sum_pairs(arr, s):
    if len(arr) < 2:
        return
    found = set()
    output = []
    for v in arr:
        diff = s - v
        if diff not in found:
            found.add(v)
        else:
            output.append([diff, v])
    print(output[0] if len(output) >0 else None)
    return output[0] if len(output) >0 else None


l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4 =[10, 5, 2, 3, 7, 5]

sum_pairs(l1, 8)
sum_pairs(l2, -6)
sum_pairs(l3, -7)
sum_pairs(l4, 10)