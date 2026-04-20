'''
Question topic - Array
Question link - 
'''
# Sol - 
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0]*n for _ in range(m)]
    def path(x,y):
        nonlocal m
        nonlocal n
        if dp[y-1][x-1]:
            return dp[y-1][x-1]
        if obstacleGrid[y][x]:
            return 0
        if x == n-1 and y == m-1:
            return 1
        if x == n-1:
            return path(x,y+1)
        if y == m-1:
            return path(x+1,y)
        temp = path(x+1,y) + path(x,y+1)
        dp[y-1][x-1] = temp
        return temp
    return path(0,0)