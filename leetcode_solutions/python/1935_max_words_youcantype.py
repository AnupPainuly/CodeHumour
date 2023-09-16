'''
Example 1:
Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.

Example 2:
Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.

Example 3:
Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.

'''
def typist(text, brokenLetters):
    list_string = text.split(' ') 
    cant_type_count = 0
    for i in list_string:
        cant_type = False
        for j in brokenLetters:
            if j in i:
                cant_type = True
                break
        if cant_type == False:
            cant_type_count += 1
    return cant_type_count

text = "leet code" 
brokenLetters = "lt"
print(typist(text, brokenLetters))
