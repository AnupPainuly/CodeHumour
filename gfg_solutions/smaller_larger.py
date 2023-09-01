'''
Input:
N = 7, X = 0
Arr[] = {1, 2, 8, 10, 11, 12, 19}
Output: 0 7
Explanation: There are no elements less or
equal to 0 and 7 elements greater or equal
to 0.
'''
def getMoreAndLess(arr,x):
    ans = [0,0] 
    for i in arr:
        if i <= x:
            ans[0] += 1
        if i >= x:
            ans[1] += 1
    return ans

if __name__ == "__main__":
    arr = [3,3,3]
    x = 3
    print(getMoreAndLess(arr,x))
