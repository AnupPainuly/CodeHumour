s = 'AA1d23cBB4'
def removeCharacters(s):
    res = ''
    for i in s:
        if i.isdigit():
            res = res + i
    return res
if __name__ == "__main__":
    print(removeCharacters(s))

