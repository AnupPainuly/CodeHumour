'''
Example 1:

Input: S = "Geeks"
Output: "Ges" 
Explanation: Deleted "e" at index 1
and "k" at index 3.

'''
def delAlternatingChar(S):
    res = ""
    for i, _ in enumerate(S):
        idx = i+1
        if idx%2 != 0:
            res +=S[idx-1]
    return res
if __name__ == "__main__":
    S = "GeeksforGeeks"
    print(delAlternatingChar(S))




