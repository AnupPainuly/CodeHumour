'''
Input:
N = 5
Arr[] = {15, 2, 45, 12, 7}
Output: 2
Explanation: Only Arr[2] = 2 exists here.

'''
arr = [15, 2, 45, 12, 7]
def valueEqualToIndex(arr):
    res = []
    for i,j in enumerate(arr):
        idx = i+1
        if idx == j:
            res.append(j)
    return res

if __name__ == "__main__":
    print(valueEqualToIndex(arr))

