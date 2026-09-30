nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]

x = 49 
ind = 0 
for el in nums:
    if(el == x):
        print("Found at index: ", ind)
    ind += 1
