def search(nums,target):
    c = 0
    for i in nums:
        c += 1
        if i == target :
            return c - 1
    return -1

t1 = [-1,0,3,5,9,12]
t2 = 9
b1 = [-1,0,3,5,9,12]
b2 = 2
print(search(b1,b2))
