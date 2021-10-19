def solution(args):
    d1, d2 = {}, {}

    for i in range(len(args)):
        try:
            if not args[i] - args[i - 1] == 1:
                d1[i] = args[i]
            if not args[i+1] - args[i] == 1 and not i == 0:
                d2[i] = args[i]
        except: pass
        # li1.append(args[-1])
    print(d1, d2)


solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])