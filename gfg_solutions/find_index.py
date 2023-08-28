'''
Input:
N = 6
arr[] = { 1, 2, 3, 4, 5, 5 }
Key = 5
Output:  4 5
Explanation:
5 appears first time at index 4 and
appears last time at index 5.
(0 based indexing)

'''
def findIndex(arr, key):
    idx = []
    for i,j in enumerate(arr):
        if j == key:
            idx.append(i)
    return idx



if __name__ == "__main__":
    arr = [23, 29, 30, 21, 16,10, 29, 27, 19, 12, 30, 20, 10, 27, 30, 24, 20, 27, 22, 16, 27, 24, 24, 11, 12, 29]
    key=29
    print(findIndex(arr,key))
