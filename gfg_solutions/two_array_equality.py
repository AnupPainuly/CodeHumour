'''
Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. 
Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.

'''
class Solution:
    def check(self,A,B,N):
        
        a = sorted(A)
        b = sorted(B)
        count = 0
        for i, j in zip(a,b):
            if i == j:
                count = count + 1
        if count == len(A):
            return True
        else:
            return False

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
