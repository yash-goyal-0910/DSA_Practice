'''
Question topic - Array
Question link - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
'''
# Sol - 
def removeDuplicates(nums):
    prev = nums[0]
    n = len(nums)
    c = 0
    i = 0
    while i != n:
        if c == 2 and nums[i] == prev:
            nums.pop(i)
            n -= 1
            continue
        elif nums[i] == prev:
            c += 1
        else:
            prev = nums[i]
            c = 1
        i += 1
    return n