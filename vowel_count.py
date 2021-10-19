def get_count(input_str):
    num_vowels = 0
    a = ['a', 'e', 'i' , 'o' , 'u']
    for letter in input_str:
        if letter in a:
            num_vowels += 1
    return num_vowels

print(get_count("abracadabra"))