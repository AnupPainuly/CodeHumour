f={}
for _ in range(int(input())):
    *prod_list, count = input().split()
    prod=" ".join(prod_list)
    count=int(count)
    if prod in f:
        f[prod]+=count
    else:
        f[prod]=count
        
for i in f:
   print(i,f[i])
