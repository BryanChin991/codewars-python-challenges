#
# def nb_year(p0, percent, aug, p):
#     count = 0
#     while True:
#         p0 = int(p0 + (p0 * percent / 100) + aug)
#         count += 1
#         if p0 >= p:
#             return count
#             exit()


def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years

nb_year(1500, 5, 100, 5000)
nb_year(1500000, 2.5, 10000, 2000000)
nb_year(1500000, 0.25, 1000, 2000000)