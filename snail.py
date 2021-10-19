def snail(snail_map):
    li = snail_map[0][:-1]

    for i in range(len(snail_map)):
        li.append(snail_map[i][-1])

    snail_map[-1].reverse()
    li.extend(snail_map[-1][1:])

    print(li)

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

array2 = [[1,2,3,1],
         [4,5,6,4],
          [7,8,9,7],
         [7,8,9,7]]

snail(array)
snail(array2)