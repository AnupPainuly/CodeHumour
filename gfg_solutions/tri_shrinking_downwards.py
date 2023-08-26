'''
Example 1:

Input:
S = Geeks
Output:
Geeks
.eeks
..eks
...ks
....s

'''
def tridown(s):
    start = 0
    end = len(s) 
    counter = 0
    for i in range(len(s)):
        print("."*counter,s[start:end], sep="")
        start += 1
        counter += 1
s= "Geeks"
tridown(s)

