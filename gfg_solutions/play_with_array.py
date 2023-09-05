'''
Given an unsorted array arr of size N, rearrange the elements of array such that number at the odd index is greater than the number at the previous even index. The task is to complete the function formatArray() which will return formatted array.

NOTE:
If the returned array formed is according to rules, 1 will be printed else 0 will be printed

Intuition:
    this fancy problem means nothing but simple sorting.
'''
# Bubble Sorting for practice
def formatArray(arr):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                has_swapped = True
    return arr

if __name__ == "__main__":
    arr = [5, 3, 2, 1, 4]
    print(formatArray(arr))
