'''
Question topic - dp,grid
Question link - https://leetcode.com/problems/unique-paths/
'''
# Sol - 
def uniquePaths(m: int, n: int) -> int:
    dp = [[0]*n for _ in range(m)]
    def path(x,y):
        nonlocal m
        nonlocal n
        if dp[y-1][x-1]:
            return dp[y-1][x-1]
        if x == n-1 or y == m-1:
            return 1
        temp = path(x+1,y) + path(x,y+1)
        dp[y-1][x-1] = temp
        return temp
    return path(0,0)