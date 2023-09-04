def convertFive(n):
    res =''
    for i in str(n):
        if i == "0":
            res = res + "5"
        else:
            res = res + i
    return res

def convertFiveI(n):
    s = str(n)
    return  s.replace("0", "5")

if __name__ == "__main__":
    n=1004
    print(convertFive(n))

