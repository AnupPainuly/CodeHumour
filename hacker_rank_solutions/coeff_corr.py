import math
arr1 = [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]
arr2 = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]

res = 0
for i in arr1:
    res = res + (i - (sum(arr1)/len(arr1)))**2 / len(arr1)
std_1 = res**(1/2)

for i in arr2:
    res = res + (i - (sum(arr2)/len(arr2)))**2 / len(arr2)
std_2 = res**(1/2)

mean_1 = sum(arr1)/len(arr1)
mean_2 = sum(arr2)/len(arr1)

corr=0

for i, j in zip(arr1, arr2):
    corr += (i - mean_1) * (j - mean_2)
corr /= (len(arr1) * std_1 * std_2)
print(round(corr,3))

