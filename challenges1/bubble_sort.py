import timeit

def bubble_sort(li):
    count=0
    while True:
        check_for_swap = False
        for i in range(len(li)):
            if i+1 <= len(li)-1:
                if li[i] > li[i+1]:
                    temp = li[i]
                    li[i] = li[i+1]
                    li[i+1] = temp
                    check_for_swap = True
        t = timeit.timeit()
        count+=1
        if not check_for_swap:
            print(f'{li}, iter: {count}, time: {t:.3}s')
            break

def sort(n, a):
    count = 0
    for i in range(n):
        swap = 0
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                count += 1
                swap += 1
        if swap == 0:
            break
    print(f'Array is sorted in {count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')

bubble_sort([5, 6, 0, 1, 2, 4, 3, 9, 8, 7])
bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

sort(3, [1, 2, 3])
sort(3, [3, 2, 1])
sort(10, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
