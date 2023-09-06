'''
two pointer algorithm to reverse the string, array. please make note the array should be sorted.

'''

def twoPointer(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(twoPointer(arr))
