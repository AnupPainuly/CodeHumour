'''
Example 1:

Input: S = "Hello"
Output: Svool
Explanation: 'H' is the 8th letter from the
beginning of alphabets, which is replaced by
'S' which comes at 8th position in reverse order
of alphabets. Similarly, all other letters are 
replaced by their respective upper or lower case 
letters accordingly.

'''
def convert(string):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_cap = alpha.upper() 
    res = ''
    for i in string:
        if i.islower():
            idx = alpha.index(i) + 1
            res += alpha[-idx]
        elif i.isupper():
            idx = alpha_cap.index(i) + 1
            res += alpha_cap[-idx]
    return res
if __name__ == "__main__":
    string="Hello"
    print(convert(string))


