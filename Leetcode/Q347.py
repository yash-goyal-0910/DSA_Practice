'''
Question topic - Array,hash
Question link - https://leetcode.com/problems/top-k-frequent-elements/description/
'''
# Sol - 
def topKFrequent(nums: List[int], k: int) -> List[int]:
    has = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in has:
            has[nums[i]] += 1
        else:
            has[nums[i]] = 1
    has = dict(sorted(has.items(), key=lambda item: item[1]))
    ans = list(has.keys())[(-1*k)::]
    return ans