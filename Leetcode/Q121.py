'''
Question topic - Array
Question link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock
'''
# Sol - 
def maxProfit(prices):
    maxi = 0
    mini = prices[0]
    for x in prices:
        mini = min(x,mini)
        if x - mini > maxi:
            maxi = x-mini
    return maxi