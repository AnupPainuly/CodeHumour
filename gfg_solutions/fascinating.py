'''
Example 1:

Input: 
N = 192
Output: Fascinating
Explanation: After multiplication with 2
and 3, and concatenating with original
number, number will become 192384576 
which contains all digits from 1 to 9.
'''
n=879
def fasc(n):
    lst = []
    lst.append(n)
    lst.append(n*2)
    lst.append(n*3)
    ca = list(map(str, lst))
    stri = "".join(ca)
    onetwonine = str([1,2,3,4,5,6,7,8,9])
    for i in stri:    
        if i not in onetwonine: 
            return True
    else:
        return False

print(fasc(n))
