'''
Question topic - dp,string
Question link - https://leetcode.com/problems/word-break/
'''
# Sol - 
def wordBreak(s: str, wordDict: List[str]) -> bool:
    dp = {}
    def words(k):
        nonlocal wordDict
        nonlocal dp
        if k == '':
            return True
        if k in dp:
            return dp[k]
        val = False
        for w in wordDict:
            if w in k:
                i = k.find(w)
                j = len(w)
                val |= words(k[:i]) and words(k[i+j:])
                if val:
                    break
        dp[k] = val
        return val
    return words(s)