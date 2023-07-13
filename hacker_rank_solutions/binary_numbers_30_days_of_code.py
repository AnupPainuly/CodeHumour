""" Objective:
    Sample Case 1: The binary representation of 5 is 101 , so the maximum number of consecutive 1's is 1.
    Sample Case 2: The binary representation of 13 is 1101 , so the maximum number of consecutive 1's is 2.
"""
bin_list = format(int(input().strip()),"b").split("0")
lengths_of_ele = []
for i in bin_list:
    lengths_of_ele.append(len(i))
print(max(lengths_of_ele))

