'''
Example:
Input:
5
2 4 1 0 6
1 2 2 0

Output:
1 1 1
'''
def searchEle(a, x):
    # Code here
    for i in a:
        if i == x:
            return True
        else:
            return False

def insertEle(a, y, yi):
    # Code here
    initial_len = len(a)
    a.insert(yi,y)
    if len(a) == initial_len + 1:
        return True
    else:
        return False

def deleteEle(a, z):
    # Code here
    try:
        a.remove(z)
        return True
    except ValueError:
        return False

#arr = [2, 4, 1, 0, 6]
arr = [801, 661, 730, 878, 305, 320]
x=736
print(searchEle(arr,x))
y, yi=444,0
print(insertEle(arr, y, yi))
z=522
print(deleteEle(arr,z))
