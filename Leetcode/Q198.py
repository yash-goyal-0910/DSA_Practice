'''
Question topic - dp,list
Question link - https://leetcode.com/problems/house-robber/
'''
# Sol - 
def rob(nums: List[int]) -> int:
    if len(nums) <= 2:
        return max(nums)
    dp = [-1]*(len(nums)+1)
    def mon(p):
        nonlocal nums
        nonlocal dp
        if p < 0:
            return 0
        if dp[p] > -1:
            return dp[p]
        temp = max(mon(p-2),mon(p-3)) + nums[p]
        dp[p] = temp 
        return temp
    return max(mon(len(nums)-1),mon(len(nums)-2))
