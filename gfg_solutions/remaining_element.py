'''
Input:
N = 7
A[] = {7, 8, 3, 4, 2, 9, 5}
Ouput:
5
Explanation:
In first step '9' would be removed, in 2nd step
'2' will be removed, in third step '8' will be
removed and so on. So the last remaining
element would be '5'.

'''
def remElement(arr):
    arr.sort()
    while True:
        if len(arr) > 1:
            arr.remove(max(arr))
        if len(arr) > 1:
            arr.remove(min(arr))
        else:
            break
    return arr[0]

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7]
    print(remElement(arr))


