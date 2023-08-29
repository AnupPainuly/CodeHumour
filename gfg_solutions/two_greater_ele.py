a  = [10, 11, 4]
# a.sort(reverse=True)
# print(a[0],a[1])
# res=[]
# for i in a:
#     if i != a[0] and i != a[1]:
#         res.append(i)
# res.sort()
# print(res)
#         
largest = float('-inf')
sec_largest = float('-inf')
for i in a:
    if i > largest:
        largest = i
for i in a:
    if i < largest and i > sec_largest:
        sec_largest = i
res = [8,7]
ans=[]
for i in a:
    if i not in res:
        ans.append(i)
ans.sort()
print(ans)

