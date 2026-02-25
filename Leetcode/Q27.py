'''
Question topic - Array
Question link - https://leetcode.com/problems/remove-element
'''
# Sol - 
def removeElement(self, nums, val):
    n = len(nums)
    i = 0
    while i != n:
        if nums[i] == val:
            nums.pop(i)
            n -= 1
            continue
        i += 1
    return len(nums)