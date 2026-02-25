'''
Question topic - Array
Question link - https://leetcode.com/problems/remove-duplicates-from-sorted-array
'''
# Sol - 
def removeDuplicates(nums):
    prev = -101
    n = len(nums)
    i = 0
    while i != n:
        if nums[i] == prev:
            nums.pop(i)
            n -= 1
            continue
        else:
            prev = nums[i]
        i += 1
    return n 