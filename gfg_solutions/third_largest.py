'''
Given an array of distinct elements. Find the third largest element in it.

Suppose you have A[] = {1, 2, 3, 4, 5, 6, 7}, its output will be 5 because it is the 3 largest element in the array A.

Example 1:

Input:
N = 5
A[] = {2,4,1,3,5}
Output: 3

'''
arr = [2,4,1,3,5]
max_val, sec_max, third_max = max(arr), float('-inf'), float('-inf')
for i in arr:
    if i < max_val and i > sec_max:
        sec_max = i
for i in arr:
    if i < sec_max and i > third_max:
        third_max = i
print(third_max)
        
