# Time Complexity: O(n2)
# Space Complexity: O(1)
number = int(input())

for i in range(2, number+1): # loop starts from 2 to previous last one
    count = True
    for j in range(2, i):
        if i % j == 0:
            count = False

    if(count == True):
        print("Prime", i)
        
    # else:
    #     # print("Not Prime",i)