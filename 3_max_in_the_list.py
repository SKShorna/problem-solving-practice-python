# Time complexity; O(n)
# Space Complexity: O(1)
num_list = [2, 1, 4, 9, 6]
max = num_list[0]


for item in num_list:
    if item > max:
        max = item
print(max)

