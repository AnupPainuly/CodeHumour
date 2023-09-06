
def findTriplet(arr,n):
    res = []
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] in arr:
                res.extend([arr[i], arr[j], arr[i]+arr[j]])
                return res
    else:
        return -1

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    n = len(arr)
    print(findTriplet(arr,n))

