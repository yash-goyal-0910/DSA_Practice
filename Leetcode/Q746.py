'''
Question topic - Array,dp
Question link - https://leetcode.com/problems/min-cost-climbing-stairs/
'''
# Sol - 
def minCostClimbingStairs(cost: List[int]) -> int:
    if len(cost) < 2:
        return 0
    dp = [-1]*len(cost)
    def mincost(k):
        nonlocal cost
        if k >= len(cost):
            return 0 
        if dp[k-1] > -1:
            return dp[k-1]
        temp = min(mincost(k+1),mincost(k+2)) + cost[k]
        dp[k-1] = temp
        return temp
    return min(mincost(0),mincost(1))