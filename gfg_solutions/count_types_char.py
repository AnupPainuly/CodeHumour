'''
Example 1:

Input:
S = "#GeeKs01fOr@gEEks07"
Output:
5
8
4
2
Explanation: There are 5 uppercase characters,
8 lowercase characters, 4 numeric characters
and 2 special characters.



'''
s = '#GeeKs01fOr@gEEks07'
low=''
up=''
num=''
spec=''
count=[]
for i in s:
    if i.islower():
        low = low + i
    elif i.isupper():
        up = up + i
    elif i.isdigit():
        num = num + i
    else:
        spec = spec + i
count.append(len(low))
count.append(len(up))
count.append(len(num))
count.append(len(spec))

