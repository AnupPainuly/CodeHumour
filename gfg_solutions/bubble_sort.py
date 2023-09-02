import time
def unoptimizedBubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def optimizedBubbleSort(arr):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] =  arr[i+1]
                arr[i+1] = temp
                has_swapped = True
    return arr
if __name__ == "__main__":
    start_time = time.time()
    arr = [5, 3, 8, 6, 7, 2]
    print(unoptimizedBubbleSort(arr))
    end_time = time.time()
    print(end_time - start_time)
