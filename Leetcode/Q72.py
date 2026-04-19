'''
Question topic - DP,string
Question link - https://leetcode.com/problems/edit-distance/
'''
# Sol - 
def minDistance( word1: str, word2: str) -> int:
    def cost(a,b):
        nonlocal word1
        nonlocal word2
        if word1[a] == word2[b]:
            return 0
        else:
            return 1
    dp = [[-1]*len(word1) for _ in range(len(word2))]
    def distance(a,b):        
        nonlocal dp
        if a == -1:
            return b+1
        if b == -1:
            return a+1
        if dp[b][a] > -1:
            return dp[b][a]
        dist = min(distance(a,b-1)+1,distance(a-1,b)+1,distance(a-1,b-1)+cost(a,b))
        dp[b][a] = dist
        return dist
    return distance(len(word1)-1,len(word2)-1)
