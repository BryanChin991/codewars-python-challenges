# def find_even_index(arr):
#     sum = 0
#     rev_sum = 0
#     li = []
#     rev_li = []
#
#     for i in arr:
#         sum += i
#         li.append(sum)
#
#     arr.reverse()
#
#     for i in arr:
#         rev_sum += i
#         rev_li.append(rev_sum)
#     rev_li.reverse()
#
#     for i in range(len(li)):
#         if li[i] == rev_li[i]:
#             return i
#             exit()
#     return -1

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

# find_even_index([1,2,3,4,3,2,1])
# find_even_index([1,100,50,-51,1,1])
# find_even_index([1,2,3,4,5,6])
# find_even_index([20,10,30,10,10,15,35])
# find_even_index([20,10,-80,10,10,15,35])
# print(find_even_index([10,-80,10,10,15,35,20]))

a = [1,2,3,4]
for i in range(len(a)):
    # print(a[:i])
    # print(sum(a[:i]))
    print(a[i+1:])
    print(sum(a[i+1:]))
