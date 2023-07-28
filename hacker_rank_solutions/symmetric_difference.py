'''
Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}

Sample Output

5
9
11
12

'''
n = int(input())
arr = set(map(int, input().split(" ")[:n]))
m = int(input())
arr1 = set(map(int, input().split(" ")[:m]))
diff = (arr1.difference(arr))
diff1 = (arr.difference(arr1))
combined_diff = sorted(diff.union(diff1))
for i in combined_diff:
    print(i)
