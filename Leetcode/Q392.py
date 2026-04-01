'''
Question topic - Array
Question link - 
'''
# Sol - 
def isSubsequence(s: str, t: str) -> bool:
    n = len(s)
    m = len(t)
    i,j = 0,0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
        j += 1
    if i == n:
        return True
    else:
        return False

isSubsequence("abc","ahbgdc")