list1 = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    list1.append([name,score])

def sorting(item):
    return (item[1],item[0])
list1.sort(key=sorting)
for i in range(1,len(list1)):
    if list1[i][1]!= list1[i-1][1]:
        secondLowestAge = list1[i][1]
        break
for item in list1:
    if item[1] == secondLowestAge:
        print(item[0])
