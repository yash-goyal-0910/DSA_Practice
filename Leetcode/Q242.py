'''
Question topic - String
Question link - https://leetcode.com/problems/valid-anagram/description/
'''
# Sol - 
def isAnagram(s: str, t: str) -> bool:
    ls = [0]*26
    for x in s:
        ls[ord(x)-97] += 1
    for x in t:
        ls[ord(x)-97] -= 1
    for i in ls:
        if i != 0:
            return False
    return True
