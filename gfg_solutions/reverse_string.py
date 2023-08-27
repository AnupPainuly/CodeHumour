'''
You are given a string s. You need to reverse the string.

Example 1:

Input:
s = Geeks
Output: skeeG

'''


s = "Geeks"
def rev(s):
    foo = s[::-1]
    return foo
print(rev(s))

def alternative_rev(s):
    foo = reversed(s) # here reversed the iterator which we have to convert to string by joining
    rev_string = "".join(foo)
    return rev_string
print(alternative_rev(s))


