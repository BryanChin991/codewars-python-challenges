def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        print(f'left: {left_arr}', end=' ')
        print(f'right: {right_arr}', end=' ')
        print()

        l, r, k = 0, 0, 0
        while l < len(left_arr) and r < len(right_arr):
            # print(l, r, k, left_arr, right_arr, arr[k])
            if left_arr[l] < right_arr[r]:
                arr[k] = left_arr[l]
                l+=1
            else:
                arr[k] = right_arr[r]
                r+=1
            k+=1

        # left element on left array
        while l < len(left_arr):
            arr[k] = left_arr[l]
            l += 1
            k += 1

        while r < len(right_arr):
            arr[k] = right_arr[r]
            r += 1
            k += 1

        print(arr)

merge_sort([2, 6, 5, 1, 7, 4, 3])

