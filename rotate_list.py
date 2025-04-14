# Add your clarifying questions here
# Will the value of shift by always be positive
# Is the list always non-empty - an empty list will return an empty list
# will the shift always be the right? yes
# What if the shift is larger number than our length? - SHift will be smaller

# input [1, 2, 3], 2
# output [2, 3, 1]

# input ['a', 'b', 'c', 'd'], 1
# output ['d', 'a', 'b', 'c']

# input ['u', 16, 'hello', 27], 3
# output ['16', 'hello', '27', 'u']

# input [9], 5233 
# output None, shift out of bounds

def rotate_list(list, shift_by):
    if not list or shift_by == 0:
        return list
    
    right_part = list[-shift_by:]
    left_part = list[:-shift_by]
    return right_part + left_part

print(rotate_list([1, 2, 3], 2))
print(rotate_list(['a', 'b', 'c', 'd'], 1))
print(rotate_list(['u', 16, 'hello', 27], 3))
print(rotate_list([], 3))