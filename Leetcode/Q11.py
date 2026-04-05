'''
Question topic - Array
Question link - https://leetcode.com/problems/container-with-most-water
'''
# Sol - 
def maxArea(height: List[int]) -> int:
    i,j = 0,len(height)-1
    width = len(height)-1
    high = 0
    maxi = 0
    while i < j:
        while height[i] <= high and  i < j:
            i += 1
            width -= 1
        while height[j] <= high and  i < j:
            j -= 1
            width -= 1
        high = min(height[i],height[j])
        temp = high*width
        maxi = max(temp,maxi)
    return maxi