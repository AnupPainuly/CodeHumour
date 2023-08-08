'''
find the index of missing number comparing two arrays
intution: avoiding loop and using sum of arrays to find the missing number.
list has index() which takes the element to give the index of the element.

'''
class Solution:
    def findExtra(self,a,b):
        total = sum(a)
        less_total = sum(b)
        missing = total - less_total
        return a.index(missing)

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b))
