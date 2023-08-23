'''
Given a string. Count the number of Camel Case characters in it.

Example 1:

Input:
S = "ckjkUUYII"
Output: 5
Explanation: Camel Case characters present:
U, U, Y, I and I.



'''
s = 'ckjkUUYII'
def detectCamel(s):
    res = ''
    for i in s:
        if i.isupper():
            res = res + i
    return res
if __name__ == '__main__':
    print(detectCamel(s))

