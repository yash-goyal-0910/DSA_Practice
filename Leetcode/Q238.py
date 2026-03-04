'''
Question topic - Array
Question link - 
'''
# Sol - 
def productExceptSelf( nums):
    prod = 1
    zero = False
    i = 0
    for x in nums:
        if x == 0:
            if zero:
                return [0]*len(nums)
            zero = True
            p_z = i
            continue
        prod *= x
        i += 1
    if zero:
        nums = ([0]*(len(nums)-1))
        nums.insert(p_z,prod)
        return nums
    else:
        for i,x in enumerate(nums):
            nums[i] = int(prod/x)
    return nums

print(productExceptSelf([-1,1,0,-3,3]))