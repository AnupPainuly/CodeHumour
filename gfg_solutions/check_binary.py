'''
check if the string is binary digits or not

'''
str="0111100110101100"
def isBinary(str):
    for i in str:
        if i != '1' and i != '0':
            return False
    return True
print(isBinary(str))

