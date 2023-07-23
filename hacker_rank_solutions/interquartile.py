'''
find IQR

'''

values = [10, 40, 30, 50, 20]
freqs = [1, 2, 3, 4, 5]
empty = []
for i,j in zip(values, freqs):
    for _ in range(j):
        empty.append(i)
sorted_empty = sorted(empty)
print('original comb list: ', sorted_empty)
lower_half = [sorted_empty[i] for i in range(len(sorted_empty)) if i < len(sorted_empty)//2 ]
upper_half = []
for i in range(len(sorted_empty)):
    if len(sorted_empty)%2 != 0:
        if i > len(sorted_empty)//2:
            upper_half.append(sorted_empty[i])
    else:
        if i > len(sorted_empty)//2 - 1:
            upper_half.append(sorted_empty[i])

print(lower_half)
print(upper_half)

def med(arr):
    mid = len(arr) // 2
    if len(arr)%2 != 0:
        res = arr[mid]
    else:
        res = (arr[mid - 1] + arr[mid])/2
    return res

q1 = med(lower_half)
q3 = med(upper_half)
iqr = q3 - q1
print(f"iqr {iqr:.2f}")
