'''
Sample Input

2 2
1 2
3 4

Sample Output

24

Explanation

The sum along axis 0 = [4 6]
The product of this sum = 24

'''
import numpy as np
n, m = map(int, input().split(" "))
lst = []
for _ in range(n):
    foo = list(map(int, input().split(" ")))
    lst.append(foo)
arr = np.array(lst)
arr_sum =np.sum(arr, axis = 0)
print(np.prod(arr_sum))
