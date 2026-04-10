'''
Question topic - Array
Question link - https://leetcode.com/problems/minimum-size-subarray-sum/description
'''
# Sol - 
def minSubArrayLen(target: int, nums: List[int]) -> int:
    i,j = 0,0
    ans = len(nums) + 1
    su = 0
    while j < len(nums) or su >= target:
        if su < target:
            su += nums[j]
            j += 1
        else:
            ans = min(ans,j-i)
            su -= nums[i]
            i += 1
    if ans == len(nums)+1:
        return 0
    return ans

print(minSubArrayLen(7,[2,3,1,2,4,3]))