def search(nums,target):
    if target in nums:
        return nums.index(target)
    return -1

t1 = [-1,0,3,5,9,12]
t2 = 9
b1 = [-1,0,3,5,9,12]
b2 = 2
print(search(t1,t2))
