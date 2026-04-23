'''
Question topic - Array,sort
Question link - https://leetcode.com/problems/h-index/description
'''
# Sol - 
def hIndex(citations: List[int]) -> int:
    n = len(citations)
    citations.sort(reverse=True)
    i = 0
    ans = 0
    while i < n:
        if ans < citations[i]:
            ans += 1
        else:
            break
        i += 1
    return ans 