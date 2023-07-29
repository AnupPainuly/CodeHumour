'''
Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output

4

sum of the set after the operations
'''
def pop_set(set_inp):
    set_inp.pop()
    return set_inp

def discard_set(set_inp, arg):
    set_inp.discard(arg)
    return set_inp
    
def remove_set(set_inp, arg):
    set_inp.remove(arg)
    return set_inp


n = int(input())
s = set(map(int, input().split(" ")[:n]))
num_operation = int(input())
op = [] 
count = 1
while count <= num_operation:
    op = list(input().split(" "))
    count += 1
    if op[0] == "pop":
        pop_set(s)
    elif op[0] == "discard":
        discard_set(s,int(op[1]))
    elif op[0] == "remove":
        remove_set(s,int(op[1]))
sum = 0
for i in s:
    sum = sum + i
print(sum)


    



