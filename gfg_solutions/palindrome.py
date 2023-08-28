'''
check if the string is palindrome
'''
s = "abba"
def palindrome(s):
    if s == s[::-1]:
        return 1
    else:
        return 0
print(palindrome(s))
