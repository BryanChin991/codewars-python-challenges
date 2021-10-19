'''def delete_nth(order,max_e):
    d = {}
    li = []
    for num in order:
        d[num] = d.get(num, 0) + 1
        if d[num] <= max_e:
            li.append(num)
    print(li)'''

def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans

delete_nth([20,37,20,21],1)
delete_nth([1,1,3,3,7,2,2,2,2],3)
delete_nth([1,1,1,1],2)