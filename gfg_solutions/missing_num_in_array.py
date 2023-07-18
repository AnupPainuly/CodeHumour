'''
N = 10
A = [6,1,2,8,3,4,7,10,5]

'''
n=int(input())
array = [2]
array.sort()
if array[0] == 1:
    missing_number = 2
    print(missing_number)
else: 
    missing_number = 1
    print(missing_number)
for i in range(min(array),n+1):
    if i not in array:
        print(i)
