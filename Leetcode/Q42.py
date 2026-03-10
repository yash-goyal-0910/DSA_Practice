'''
Question topic - Array
Question link - https://leetcode.com/problems/trapping-rain-water
'''
# Sol - 
def trap(height: List[int]) -> int:
    n = len(height)
    ls = [0]*n
    depth = 0
    i,j = 0,n-1
    while i < j:
        while height[i] <= depth and i < j:
            i += 1
        while height[j] <= depth and i < j:
            j -= 1
        depth = min(height[i],height[j])
        for x in range(i,j+1):
            ls[x] = depth

    if depth == 0 or n == 1:
        return 0

    ans = 0
    for i,x in enumerate(height):
        ans += ls[i] - x

    return ans

trap([0,1,0,2,1,0,1,3,2,1,2,1])