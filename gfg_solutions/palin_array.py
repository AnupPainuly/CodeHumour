'''
Example 1:

Input:
5
111 222 333 444 555

Output:
1

Explanation:
A[0] = 111 //which is a palindrome number.
A[1] = 222 //which is a palindrome number.
A[2] = 333 //which is a palindrome number.
A[3] = 444 //which is a palindrome number.
A[4] = 555 //which is a palindrome number.
As all numbers are palindrome so This will return 1.

'''
def palinArray(arr):
    mod = list(map(str, arr))
    for i in mod:
        if i != i[::-1]:
            return 0
    else:
        return 1
            
if __name__ == "__main__":
    arr = [111, 222, 333, 444, 555]
    print(palinArray(arr))

