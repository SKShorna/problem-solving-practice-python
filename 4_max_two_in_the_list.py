# Time complexity;  O(2n)
# Space Complexity: O(1)
num_list = [2, 1, 4, 9, 6]
print(num_list)

# to take input from user
# num_list = input().split()
# num_list = list(map(int, num_list))
# print(num_list)
# Select 1st number as a max from the list
max = num_list[0]

# take a variable for the position of the list value (index value)
pos = 0

# 1st for loop for first largest number
for i in range(len(num_list)):
    if num_list[i] > max:
        max = num_list[i]
        #hold position of the max number index
        pos = i 
print("First largest value in the list",max)
num_list[pos] = -1 # to replace the current largest values, set it as lowest number to find out second largest value in the list

max = num_list[0]
pos = 0

for i in range(len(num_list)):
    if num_list[i] > max:
        max = num_list[i]
print("Second largest value in the list", max)
