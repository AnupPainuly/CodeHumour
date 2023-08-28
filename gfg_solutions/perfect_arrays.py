'''
Input : Arr[] = {1, 2, 3, 2, 1}
Output : PERFECT
Explanation:
Here we can see we have [1, 2, 3, 2, 1] 
if we reverse it we can find [1, 2, 3, 2, 1]
which is the same as before.
So, the answer is PERFECT.
'''
def isPerfect(arr):
    if arr == arr[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    arr = [1,2,3,2,1]
    if isPerfect(arr):
        print("PERFECT")
    else:
        print("NOT PERFECT")
