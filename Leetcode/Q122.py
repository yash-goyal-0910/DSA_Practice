'''
Question topic - Array
Question link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
'''
# Sol - 
def maxProfit(prices):
    prev = prices[0]
    profit = 0
    for x in prices[1::]:
        if prev < x:
            profit += x - prev
            prev = x
        else:
            prev = x
    return profit