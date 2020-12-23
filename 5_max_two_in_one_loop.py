# Time Complexity: O(N)
# Space Complexity: O(1)

num_list = input().split()
num_list  = list(map(int, num_list))
print(num_list)

# sample list 
# num_list = [-4, -3, 0, 1, 2, -5]
# consider for 1st largest number in the list
max_1 = num_list[0]

# consider for the 2nd largest number in the list
max_2 = num_list[1]

# check and swap number before finding the 1st and 2nd number from the list
if max_2 > max_1:
    temp = max_1
    max_1 = max_2
    max_2 = temp

# start checking from third number (index 2)
for i in range(2, len(num_list)):
    # check the third number greater than max_1  
    # max_1 = -4, max_2= -3, third num = 0; set max_2 = max_1 (-4) and max_1 = 0
    # 4 1 3
    if num_list[i] > max_1:
        max_2 = max_1
        max_1 = num_list[i]
    # check third number greater than max_2 
    # max_2= 10, third num = 11 ; set max_2 = third num (11)
    elif num_list[i] > max_2:
        max_2 = num_list[i]
         
print(max_1)
print(max_2)