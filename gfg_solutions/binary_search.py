'''
binary search using recursion

'''
def binSearch(arr, key, first_index, last_index):
    mid_index = (first_index + last_index) // 2
    mid_ele = arr[mid_index]
    if last_index >= first_index:
        if mid_ele == key:
            return mid_ele
        elif mid_ele > key:
            new_position = mid_index - 1
            return binSearch(arr, key, first_index, new_position)
        elif mid_ele < key:
            new_position = mid_index + 1
            return binSearch(arr, key, new_position, last_index)
    else:
        return -1
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    key = int(input("enter the key to search: "))
    first_index, last_index = 0, len(arr) - 1
    if binSearch(arr, key, first_index, last_index) == -1:
        print("invalid key")
    else:
        print(binSearch(arr,key,first_index,last_index))

