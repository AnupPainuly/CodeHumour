'''
For Example:

Input:
A[] = {11,12,13,14,15}, k=1
Output:
6 
Explanation: Here digit 1 appears in the whole array 6 times.

'''
def num(arr, k):
    str_arr = list(map(str,arr))
    count = 0
    for i in str_arr:
        for j in i:
            if j == str(k):
                count += 1
    return count

if __name__ == "__main__":
    arr = [11,12,13,14,15]
    k=1
    print(num(arr, k))
