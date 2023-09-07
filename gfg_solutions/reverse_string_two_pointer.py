'''
using two pointer algorithm to reverse the string
'''
string = "GeeksforGeeks"
arr = list(string)
start, end = 0, len(arr) - 1 
while start < end: # when start becomes more than end that mean pointers has overlapped
    arr[start], arr[end] = arr[end], arr[start] # swapping
    start += 1 # moving pointer
    end -= 1 # moving pointer

print("".join(arr))

