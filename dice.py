'''def score(dice):
    score = 0
    if 1 in dice:
        if dice.count(1) < 3:   score += dice.count(1)*100
        if dice.count(1) == 3:   score += 1_000
        if dice.count(1) > 3:   score += (dice.count(1)-3)*100+1_000
    if 5 in dice:
        if dice.count(5) < 3:   score += dice.count(5)*50
        if dice.count(5) == 3:   score += 500
        if dice.count(5) > 3:   score += (dice.count(5)-3)*50+500
    for i in range(2, 7, 1):
        if i != 5:
            if dice.count(i) >= 3:     score += i*100
    print(score)'''


def score(dice):
    sum = 0
    counter = [0, 0, 0, 0, 0, 0]
    points = [1000, 200, 300, 400, 500, 600]
    extra = [100, 0, 0, 0, 50, 0]
    for die in dice:
        counter[die - 1] += 1

    for (i, count) in enumerate(counter):
        sum += (points[i] if count >= 3 else 0) + extra[i] * (count % 3)

    return sum

score([2, 3, 4, 6, 2])
score([4, 4, 4, 3, 3])
score([2, 4, 4, 5, 4])

score([5, 1, 3, 4, 1])
score([1, 1, 1, 3, 1])
score([2, 4, 4, 5, 4])

score([3, 3, 3, 3, 3])
score([6, 6, 6, 3, 3])

