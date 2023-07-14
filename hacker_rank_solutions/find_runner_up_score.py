'''
Objective: finding the second largest number in the list

'''


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(" ")[:n]))
    # start with assumption that first ele is max and second ele is second_max
    max_num = arr[0]
    second_max = arr[1]
    for i in range(2, len(arr)):
        if arr[i] > max_num:
            second_max = max_num
            max_num = arr[i]
        elif arr[i] > second_max and arr[i] != max_num:
            second_max = arr[i]
    print(second_max)

