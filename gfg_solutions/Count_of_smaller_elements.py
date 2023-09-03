'''
Input:
N = 6
A[] = {1, 2, 4, 5, 8, 10}
X = 9
Output:
5

'''

def countOfEle(arr, key):
    res = []
    for i in arr:
        if i <= key:
            res.append(i)
    return len(res)


if __name__ == "__main__":
    arr = [1,2,4,5,6,10]
    key = 9
    print(countOfEle(arr, key))
