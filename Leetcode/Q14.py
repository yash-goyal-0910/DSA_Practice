'''
Question topic - String
Question link - https://leetcode.com/problems/longest-common-prefix/
'''
# Sol - 
def longest_common_prefix(strs):
    longest = strs[0]
    for x in strs:
        t = min(len(longest),len(x))
        longest = longest[:t:]
        for i in range(t):
            if longest[i] != x[i]:
                longest = longest[:i:]
                break
    return longest