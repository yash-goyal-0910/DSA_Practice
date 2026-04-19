'''
Question topic - dp,list
Question link - https://leetcode.com/problems/climbing-stairs/
'''
# Sol - 
def climbStairs(n: int) -> int:
    dp = [0] * (n+1)
    def climb(x):
        nonlocal dp
        if x == 0 or x == 1:
            return 1
        elif dp[x] > 0:
            return dp[x]
        temp = climb(x-2) + climb(x-1)
        dp[x] = temp
        return temp
    return climb(n)
        