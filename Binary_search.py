def search(nums,target):
    l = 0
    r = len(nums) -1
    for i in range(len(nums)) :
        if nums[l] == target :
            return l
        elif nums[l] < target:
            l += 1
        if nums[r] == target:
            return r
        elif nums[r] > target:
            r -= 1
    return -1

#test case
t1 = [-1,0,3,5,9,12]
t2 = 9
b1 = [-1,0,3,5,9,12]
b2 = 2
c1 = [-1,0,1]
c2 = -1
d1 = [5]
d2 = 5
e1 =[-1,0,3,5,9,12]
e2 = 13
a1 = [-1,0,3,5,9,12]
a2 = 9
print(search(a1,a2))
