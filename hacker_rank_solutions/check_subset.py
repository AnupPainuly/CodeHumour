'''
Sample Input

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

Sample Output

True 
False
False

Explanation

Test Case 01 Explanation

Set A = {1 2 3 5 6}
Set B = {9 8 5 6 3 2 1 4 7}
All the elements of set A are elements of set B .
Hence, set A is a subset of set B .


'''
if __name__ == "__main__":
    test_cases = int(input())
    count = 0
    while count < test_cases:
        n = int(input())
        set_a = set(map(int, input().split(" ")[:n]) )
        n = int(input())
        set_b = set(map(int, input().split(" ")[:n]) )
        print(set_a.issubset(set_b))
        count += 1
