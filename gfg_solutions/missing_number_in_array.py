'''
finding the missing number from an array
Intuition: sum of n natural numbers ```n*(n+1) // 2```

'''
class Solution:
    def missingNumber(self,array,n):
        print("org arr sum", sum(array))
        total = n*(n+1) // 2
        return total -sum(array)
        
t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
