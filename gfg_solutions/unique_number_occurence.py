'''
POTD
Input:
N = 5
arr = [1, 1, 2, 5, 5]
Output:
false
Explanation:
The array contains 2 (1’s), 1 (2’s) and 2 (5’s), 
since the number of frequency of 1 and 5 are the same i.e. 2 times. 
Therefore, this array does not satisfy the condition.
'''
from collections import Counter
def freq(arr):
    counter = dict(Counter(arr))
    if len(counter.values()) == len(set(counter.values())):
        return True
    else:
        return False

arr = list(map(int, input().split(" ")))
print(freq(arr))
