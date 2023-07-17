def average(array):
    arr = set(array)
    avg = sum(arr)/len(arr)
    print(avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(" ")[:n]))
    average(arr)
