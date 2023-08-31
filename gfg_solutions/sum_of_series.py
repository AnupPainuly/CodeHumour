'''
Input:
N = 5
Output: 15
Explanation: For n = 5, sum will be 15.
1 + 2 + 3 + 4 + 5 = 15.
'''
def series(n):
    return format(int(n*(n+1)/2)) # using formula
n=5
print(series(n))

