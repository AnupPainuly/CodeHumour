if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(" ")[:n]))
    print(arr)
    # assume that the first element is maximun
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    print(max)



