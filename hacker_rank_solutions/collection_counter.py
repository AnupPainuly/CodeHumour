from collections import Counter
no_of_shoes = int(input())
sizes = list(input().split())
shoe_sizes = Counter(sizes)
cust = int(input())
cost = 0

for _ in range(cust):
    size, price = input().split()
    if size in shoe_sizes.keys() and shoe_sizes[size]>0:
        cost = cost + int(price)
        shoe_sizes[size] -= 1
print(cost)
