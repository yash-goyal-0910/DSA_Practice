'''
Question topic - Array
Question link - https://leetcode.com/problems/jump-game
'''
# Sol - 
def canJump(nums):
    n = len(nums) - 1
    j = 1
    i = 0
    while j > i and i <= n:
        j = max(i+1+nums[i],j)
        i += 1
    if j > n:
        return True
    else:
        return False
print(canJump([1,2,3]))
        
        