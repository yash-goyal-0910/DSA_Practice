'''
Question topic - Array
Question link - https://leetcode.com/problems/candy
'''
# Sol - 
def candy(ratings: List[int]) -> int:
    n = len(ratings)
    candies = [1] * n
    count = 0
    for i in range(1,n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    for i in range(n-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i],candies[i+1]+1)
        count += candies[i]
    return count + candies[-1]

candy([1,2,2])