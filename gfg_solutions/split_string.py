'''
Input:
S = geeks01for02geeks03!!!
Output:
geeksforgeeks
010203
!!!
Explanation: The output shows S1, S2 and S3. 
'''
def splitString(s):
    res = []
    alpha, num, spec = '', '', ''
    for i in s:
        if i.isalpha():
            alpha += i
        elif i.isdigit():
            num += i
        else:
            spec += i
    res.append(alpha)
    res.append(num)
    res.append(spec)
    return res
if __name__ == "__main__":
    s = "geeks01for02geeks03!!!"
    print(splitString(s))
