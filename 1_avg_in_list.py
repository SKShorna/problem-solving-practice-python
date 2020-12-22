# input would be a string 
user_num = input("Enter numbers: ")
print("\n")

# split the input into list
user_list = user_num.split()

# convert string list to integer list
user_list = list(map(int, user_list))
print(user_list)

sum = 0
# to count the odd number in the list
odd_counter = 0

for num in user_list:
  # true only for the odd numbers
  if num % 2 != 0:
    odd_counter += 1 # increment the counter by 1
    sum = sum + num  # add the odd number to the sum
avg = sum / odd_counter 
print(avg)
