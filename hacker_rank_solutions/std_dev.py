'''
Task
Given an array, arr , of n integers, calculate and print the standard deviation. 
Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format). 
An error margin of +- 0.1 will be tolerated for the standard deviation.

'''
def std_dev(arr):
    summation = 0
    mean = sum(arr)/len(arr)
    for i in arr:
        summation = summation + (i - mean)**2
    print(round((summation/len(arr))**(1/2), 1))


if __name__ == "__main__":
    n = int(input())
    sample = list(map(int, input().split(' ')[:n]))
    std_dev(sample)


