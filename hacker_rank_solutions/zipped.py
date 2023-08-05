'''
Output Format

Print the averages of all students on separate lines.

The averages must be correct up to

decimal place.

Sample Input

5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

Sample Output

90.0 
91.0 
82.0 
90.0 
85.5        


'''
students, sub = map(int, input().split(" ")) 
foo = []
for _ in range(sub):
    marks = list(map(float, input().split(" ")[:students]))
    foo.append(marks)

for i in zip(*foo):
    print(sum(i)/sub)


