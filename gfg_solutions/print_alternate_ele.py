'''
Input:
N = 4
A[] = {1, 2, 3, 4}
Output:
1 3
'''
def alterEle(arr):
    res = []
    for i, j in enumerate(arr):
        idx = i+1
        if idx % 2 != 0:
            res.append(j)
    return res

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(alterEle(arr))
