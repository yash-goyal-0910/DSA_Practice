'''
Question topic - Array
Question link - https://leetcode.com/problems/majority-element
'''
# Sol - 
def majorityElement(nums):
    candidate = nums[0]
    count = 0
    for x in nums:
        if x == candidate:
            count += 1
        else:
            if count == 0:
                candidate = x
                count = 1
            else:
                count -= 1
    return candidate