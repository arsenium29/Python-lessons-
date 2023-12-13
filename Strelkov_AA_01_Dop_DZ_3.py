# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
def move_zeros_to_end(arr):
    zeros = []
    non_zeros = []
    
    for num in arr:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
    
    return non_zeros + zeros
print(move_zeros_to_end([1,1,1,1,0,11,1,1,0,1,]))