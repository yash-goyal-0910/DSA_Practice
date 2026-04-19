'''
Question topic - Array,dp
Question link - https://leetcode.com/problems/coin-change/description/
'''
# Sol - 
def coinChange(coins: List[int], amount: int) -> int:
    dp = [0]*(amount+1)
    def change(k):
        if k < 0:
            return 100000
        elif k == 0:
            return 0
        if dp[k] > 0:
            return dp[k]
        temp = 100000
        for c in coins:
            temp = min(change(k-c)+1,temp)
        dp[k] = temp
        return temp
    var = change(amount)
    if var == 100000:
        return -1
    return var

