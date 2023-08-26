'''
Example 1:

Input:
S = "ab C"
Output:
zy X
Explanation:
The reciprocal of the first letter 'a' is 'z'.
The reciprocal of the second letter 'b' is 'y'.
The reciprocal of the third letter ' ' is ' '.
The reciprocal of the last letter 'C' is 'X'.

'''
def reciprocalOfString(S):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_cap = alpha.upper()
    res = ""
    for i in S:
        if i in alpha:
            idx = alpha.index(i) + 1
            res += alpha[-idx]
        elif i in alpha_cap:
            idx = alpha_cap.index(i) + 1
            res += alpha_cap[-idx]
        else:
            res += i
    return res

S = "Ish"
print(reciprocalOfString(S))



