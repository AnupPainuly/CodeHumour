'''
Intuition: sliding window

Input:
The first line of input is an integer T denoting the no of test cases. Then T test casesfollow . The first line of each test case are two integer N and K separated by space .The next line contains N space separated values of the array A[ ].

Output:
Output of each test case will be an integer denoting the largest product of subarray of size k.

Constraints:
1 <=T<= 100
1 <=N<= 10
1 <=K<= N
1<=A[]<=10

Example:
Input
1
4 2
1 2 3 4
Output
12
'''
arr = [1,2,3,4]
def slidingWindow(arr, window_size):
    max_product = float('-inf')
    product = 1
    if len(arr) <= window_size:
        for i in arr:
            product *= i
        max_product = max(product, max_product)
        return max_product
    for i in range(len(arr) - window_size + 1):
        product = 1
        subarray = arr[i : i + window_size]
        for i in subarray:
            product *= i
        max_product = max(product, max_product)
    return max_product

window_size = 2
print(slidingWindow(arr, window_size))

