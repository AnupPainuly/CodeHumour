'''
Task
Given an integer, n,n and space-separated integers as input, create a tuple, t , of those integers. 
Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

'''
n = int(input())
t = tuple(map(int, input().split(" ")[:n]))
print(hash(t))
