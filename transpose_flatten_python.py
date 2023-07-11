"""
Objective:

You are given a N X M integer array matrix with space separated elements (N = rows and M= columns).
Your task is to print the transpose and flatten results.

Input Format:
The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of M columns.

Output Format:
First, print the transpose array and then print the flatten.

"""

import numpy as np
n, m = map(int, input().split(" ")) 
arr = []
for i in range(n):
    elements = list(map(int,input().split(" ")))
    arr.append(elements)
num_arr = np.array(arr)
print(np.transpose(num_arr))
print(num_arr.flatten())
