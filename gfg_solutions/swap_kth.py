'''
Input:
N = 8, K = 3
Arr[] = {1, 2, 3, 4, 5, 6, 7, 8}
Output: 1 2 6 4 5 3 7 8
Explanation: Kth element from beginning is
3 and from end is 6.
'''
def swap_kth(arr,k):
    temp = 0
    temp = arr[k-1]
    arr[k-1] = arr[-k]
    arr[-k] = temp
    return arr


if __name__ == "__main__":
    k = 3
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(swap_kth(arr,k))

