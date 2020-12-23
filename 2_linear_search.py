# time complexity: O(n)
# Space complexity O(1)

num_list = [2, 4, 5, 7, 8]

item = 2

# flag 
found = False

for i in range(len(num_list)):
    if item == num_list[i]:
        print(i, end = " ")
        print(num_list[i])
        found = True

if not found: # found == False
   print("Item not found")




  

    