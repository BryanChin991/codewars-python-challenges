def bouncing_ball(h, bounce, window):
    import math
    return (int(math.log((window / h), bounce)) * 2 + 1 if window / h != bounce else 1) if h > 0 and 0 < bounce < 1 and window < h else -1



print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(3, 1, 1.5))
print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(30, 0.66, 1.5))
print(bouncing_ball(40, 1, 10))
