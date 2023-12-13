# An array consisting of 0s and 1s, also called a binary array, is given as an input. 
 
# Task 
# Find the length of the longest contiguous subarray which consists of equal number of 0s and 1s. 
 
# Example 
# s = [1,1,0,1,1,0,1,1] 
#          |_____| 
#             | 
#          [0,1,1,0] 
 
#          length = 4 
# Note 
# 0 <= length(array) < 120 000
def find_longest_subarray(arr):
    count = {0: -1}
    max_length = 0
    cumulative_count = 0

    for i, num in enumerate(arr):
        if num == 0:
            cumulative_count -= 1
        else:
            cumulative_count += 1

        if cumulative_count in count:
            length = i - count[cumulative_count]
            max_length = max(max_length, length)
        else:
            count[cumulative_count] = i

    return max_length
s = [1, 1, 0, 1, 0, 0, 1, 0, 1, 1]
print(find_longest_subarray(s))