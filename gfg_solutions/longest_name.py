'''
display the longest string from the list of strings.

intuition:
    max function first sorts the list. in case of strings max function uses lexographical sorting hence, we have to provide key parameter.

'''
names = ["abc" ,"cb", "a"]
print(max(names, key=len))
