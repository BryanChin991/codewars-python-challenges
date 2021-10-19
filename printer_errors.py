# def printer_error(s):
#     li = []
#     count = 0
#     total = 0
#
#     for i in range(97, 110, 1):
#         li.append(chr(i))
#
#     for letter in s.lower():
#         if letter not in li:
#             count += 1
#         total += 1
#     string = str(count) + '/' + str(total)
#     return string

from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

print(printer_error('kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu'))
