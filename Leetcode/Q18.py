'''
Question topic - Array
Question link - https://leetcode.com/problems/4sum/
'''
# Sol - 
def proper_nums(nums):
    nums = sorted(nums)
    i = 0
    e = nums[0]
    c = 0
    while i < len(nums):
        if nums[i] == e:
            if c < 4:
                c += 1
            else:
                nums.pop(i)
                i -= 1
        else:
            e = nums[i]
            c = 1
        i += 1
    return nums
def fourSum(nums, target: int):
    sol = []
    sol_set = []
    nums = proper_nums(nums)
    n = len(nums)
    if n < 4:
        return []
    for i in range(0,n-3,1):
        for j in range(i+1,n-2,1):
            for k in range(j+1,n-1,1):
                for l in range(k+1,n,1):
                    if (nums[i] + nums[j] + nums[k] + nums[l]) == target:
                        x = [nums[i] ,nums[j] ,nums[k] ,nums[l]]
                        if x not in sol:
                            y = set(x)
                            if y not in sol_set:
                                sol.append(x)
                                sol_set.append(y)
    return sol
nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums,target))