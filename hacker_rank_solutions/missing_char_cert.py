def miss(s):
    lst = []
    for letter in '1234567890abcdefghijklmnopqrstuvwxyz':
        if letter not in s: 
            lst.append(letter)
    lst.sort()
    new = ''.join(lst)
    return new

s = input()
print(miss(s))
