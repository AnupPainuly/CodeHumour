'''
Input: 
S = "practice"
Output: prectica
Explanation: The vowels are a, i, e
Reverse of these is e, i, a.

'''
s = "practice"
def vow_rev(s):
    vow = ['a','i','o','e','u']
    extr_vow=''
    for i in s:
        if i in vow:
            extr_vow += i
    reversed_vow = extr_vow[::-1]
    reversed_str=''
    idx = 0
    for i in s:
        if i in vow:
            reversed_str += reversed_vow[idx]
            idx += 1
        else:
            reversed_str += i
    return reversed_str

if __name__ == "__main__":
    print(vow_rev(s))




