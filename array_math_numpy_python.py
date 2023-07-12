'''
Sample Input

1 4
1 2 3 4
5 6 7 8

Sample Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 

'''
import numpy as np
n, m = map(int, input().split(" "))
n_arr1 = np.array([ list(map(int, input().split(" "))) for _ in range(n) ])
n_arr2 = np.array([ list(map(int, input().split(" "))) for _ in range(n) ])

#numpy operations

print(np.add(n_arr1, n_arr2))
print(np.subtract(n_arr1, n_arr2))
print(np.multiply(n_arr1, n_arr2))
print(np.floor_divide(n_arr1, n_arr2))
print(np.mod(n_arr1, n_arr2))
print(np.power(n_arr1, n_arr2))

