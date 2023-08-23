S = "welcome to geeksforgeeks"
def removeVow(S):
    vow = [ 'a','i','e','o','u' ]
    res = ''
    for i in S:
        if i not in vow:
            res = res + i
    return res
if __name__ == "__main__":
    print(removeVow(S))



