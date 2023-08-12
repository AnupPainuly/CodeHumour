'''
kadanes alogrithm to find the maximum sum amongst all the possible contigous sub arrays in given array

'''
a = [-2, 4, -3 -1, -2]
local_max_sum, global_max_sum = 0, float('-inf')
for i in a:
    local_max_sum = local_max_sum + i
    if local_max_sum > global_max_sum:
        global_max_sum = local_max_sum
    if local_max_sum < 0:
        local_max_sum = 0
print(global_max_sum)
