'''
Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

4

'''
n = int(input())
set_a = set(map(int, input().split(" ")[:n]))
m = int(input())
set_b = set(map(int, input().split(" ")[:m]))
print(len(set_a.difference(set_b)))
