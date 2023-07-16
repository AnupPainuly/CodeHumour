'''
Input:
4
4 3 2 1 
Output: 
1 2 3 4
Explanation: 
After reversing the given elements of the queue , the resultant queue will be 1 2 3 4.

'''

from queue import Queue
n=int(input())
a=list(map(int,input().split()))
q=Queue(maxsize=n)
for j in a:
    q.put(j)

temp_list = []
while not q.empty():
    temp_list.append(q.get())
for i in temp_list[::-1]:
    q.put(i)
while not q.empty():  
    ele = q.get()
    print(ele,end=' ')

'''
Conclusion:
Take an empty list
Pop elements from queue until its empty and push them to list
Traverse from back side of list and again add them to queue.

'''
