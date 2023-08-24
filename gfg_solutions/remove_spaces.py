'''
Example 1:

Input:
S = "geeks  for geeks"
Output: geeksforgeeks
Explanation: All the spaces have been 
removed.

'''
s = "string with spaces"
foo = s.replace(" ","")
print(foo)
res = ''
for i in s:
    if i != " ":
        res = res + i
print(res)


