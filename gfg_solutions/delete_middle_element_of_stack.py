lst = [10, 20, 30, 40, 50]
if len(lst) % 2 == 0:
    mid = len(lst)//2 - 1
    lst.pop(mid)
else:
    mid = len(lst)//2
    lst.pop(mid)
for i in range(len(lst)-1,-1,-1):
    print(lst[i],end=' ')

