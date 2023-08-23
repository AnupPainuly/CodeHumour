'''
Given a list of characters, merge all of them into a string.

Example 1:

Input:
N = 13
Char array = g e e k s f o r g e e k s
Output: geeksforgeeks 
Explanation: combined all the characters
to form a single string.

'''

def chartostr(arr):
    foo = ''.join(arr)
    return foo
arr = ['g','e','e','k','s']
if __name__ == "__main__":
    print(chartostr(arr))

