'''
Question topic - Array,dp
Question link - https://leetcode.com/problems/longest-increasing-subsequence/
'''
# Sol - 
def lengthOfLIS(nums: List[int]) -> int:
    dp = [0] * (len(nums)+1)
    def substr(k):
        nonlocal dp
        if dp[k] > 0:
            return dp[k]
        val = 1
        for i in range(k):
            if nums[i] < nums[k]:
                val = max(val,substr(i)+1)
        dp[k] = val
        return val
    ma = 0
    for i in range(len(nums)-1,-1,-1):
        x = substr(i)
        if x > ma:
            ma = x                    
    return ma