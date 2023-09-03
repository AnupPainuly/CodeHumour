'''
Given a sorted array of size N and an integer K, find the position(0-based indexing) at which K is present in the array using binary search.

Example 1:

Input:
N = 5
arr[] = {1 2 3 4 5} 
K = 4
Output: 3
Explanation: 4 appears at index 3.

'''
def binarySearch(arr, key, first_index, last_index):
    if last_index >= first_index:
        mid_index = (first_index + last_index) // 2
        if arr[mid_index] == key:
            return mid_index
        elif arr[mid_index] > key:
            new_position = mid_index - 1
            return binarySearch(arr, key, first_index , new_position)
        elif arr[mid_index] < key:
            new_position = mid_index + 1
            return binarySearch(arr, key, new_position , last_index)
    else:
        return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    key = 4
    first_index, last_index = 0, len(arr) - 1
    print(binarySearch(arr, key, first_index, last_index))

