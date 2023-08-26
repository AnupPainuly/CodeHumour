'''
Input: S = "ABCddE"
Output: "abcdde"
Explanation: A, B, C and E are converted to
a, b, c and E thus all uppercase characters 
of the string converted to lowercase letter.
'''
def toLower(s):
    res = ""
    for i in s:
        if i.isupper():
            res += i.lower()
        else:
            res += i
    return res
if __name__ == "__main__":
    s = "ABCddE"
    print(toLower(s))

