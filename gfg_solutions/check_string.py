'''
Given a string, check if all its characters are the same or not.

Example 1:

Input:
s = "geeks"
Output: False
Explanation: The string contains different
character 'g', 'e', 'k' and 's'.


'''
s='ggg'
def check(s):
    for i in s:
        if s[0] != i:
            return False
    return True

if __name__ == "__main__":
    print(check(s))
