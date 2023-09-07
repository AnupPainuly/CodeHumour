'''
two pointer approach to shift zeroes to the end.
'''
def moveZeroToEnd(arr):
    j=0 # j tracks the element which are zero. lagging
    for i in range(len(arr)):
        if arr[i] != 0 and arr[j] == 0:
            arr[j], arr[i] = arr[i], arr[j] # swapping if zero, non-zero
        if arr[j] != 0:
            j += 1
    return arr


if __name__ == "__main__":
    arr = [1,2,0,3,0,4,0]
    print(moveZeroToEnd(arr))
