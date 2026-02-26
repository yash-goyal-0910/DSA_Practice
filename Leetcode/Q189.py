'''
Question topic - Array
Question link - https://leetcode.com/problems/rotate-array
'''
# Sol - 
def rotate(nums, k: int):
    for x in range(k):
        nums.insert(0,nums.pop())