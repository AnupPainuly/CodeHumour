'''
Input Format

The first line contains the space separated values of N and M.
The next N lines contains M space separated integers.

Output Format

First, print the mean.
Second, print the var.
Third, print the std.

Sample Input

2 2
1 2
3 4

Sample Output

[ 1.5  3.5]
[ 1.  1.]
1.11803398875


'''


import numpy as np
n, m = map(int, input().split(" "))
arr = np.array([ list(map(int, input().split(" "))) for _ in range(n) ])
print(np.mean(arr, axis = 1),np.var(arr, axis = 0),round(np.std(arr),11), sep='\n')


