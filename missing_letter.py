'''def find_missing_letter(chars):
    li = []
    for char in chars:
        li.append(ord(char))
    for i in range(li[0], li[len(li) -1], 1):
        if i not in li:
            return chr(i)'''
def find_missing_letter(chars):
    return [chr(n) for n in range(ord(chars[0]),ord(chars[-1])+1) if n not in [ord(c) for c in chars]][0]

print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter(["O","Q","R","S"]))
