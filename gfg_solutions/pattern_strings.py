'''
Example 1:

Input: S = "GeeK"
Output: Geek
        Gee
        Ge
        G
Explanation: Decrease one character 
after each line
'''
S="Geek"
start,counter = 0, 0
end = len(S)
foo = []
while counter < len(S):
    if len(S) == 1:
        foo.append(S)
        break
    foo.append(S[start:end])
    end = end- 1
    counter = counter + 1
print(foo)
    	    
