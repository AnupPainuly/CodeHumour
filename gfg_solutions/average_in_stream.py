'''
Input:
n = 5
arr[] = {10, 20, 30, 40, 50}
Output: 10.00 15.00 20.00 25.00 30.00 
Explanation: 
10 / 1 = 10.00
(10 + 20) / 2 = 15.00
(10 + 20 + 30) / 3 = 20.00
And so on.
'''
def avgOfStream(arr,):
    count = 0
    start, end = 0,1
    mean = []
    while count < len(arr):
        avg = sum(arr[start:end]) / len(arr[start:end])
        mean.append(avg)
        count += 1
        end +=1
    return mean

if __name__ == "__main__":
    arr= [10, 20, 30, 40, 50]
    print(avgOfStream(arr))

