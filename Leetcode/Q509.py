'''
Question topic - Array,dp
Question link - https://leetcode.com/problems/fibonacci-number/
'''
# Sol - 
def fib(n: int) -> int:
    dp = [0]*n
    def F(k):
        nonlocal dp
        if k == 0 or k == 1:
            return k
        if dp[k-1] > 0:
            return dp[k-1]
        temp = F(k-1) + F(k-2)
        dp[k-1] = temp
        return temp
    return F(n)
