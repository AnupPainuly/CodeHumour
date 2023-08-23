'''
Example 1:

Input:
s = "1: Prakhar Agrawal, 2: Manish Kumar Rai, 
     3: Rishabh Gupta56"
Output: 1 2 3 56
Explanation: 
1, 2, 3, 56 are the integers present in s.

'''
import re
s = "1: Prakhar Agrawal, 2: Manish Kumar Rai, 3: Rishabh Gupta56"
def extr(s):
    temp = re.findall(r'[0-9]+', s)
    res = list(map(str, temp)) #storing as int in list removes 0 if the input is B<03
    return str(res)
print(extr(s))

