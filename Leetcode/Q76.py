'''
Question topic - Sliding Window
Question link - https://leetcode.com/problems/minimum-window-substring/description
'''
# Sol - 
def minWindow(s: str, t: str) -> str:
    i,j = 0,0
    dic = dict()
    posi_ans = []
    for x in t:
        if x in dic:
            dic[x] -= 1
        else:
            dic[x] = 0
    valid = False
    while j < len(s) or valid:
        if valid:
            if s[i] in dic:
                dic[s[i]] -= 1
                if dic[s[i]] < 1:
                    posi_ans.append(s[i:j])
                    valid = False
            i += 1
        else:
            if s[j] in dic:
                dic[s[j]] += 1
                valid = True
                for x in dic.keys():
                    if dic[x] < 1:
                        valid = False
                        break
            j += 1
    if posi_ans:
        return min(posi_ans,key=len)
    return ''
print(minWindow("ADOBECODEBANC","ABC"))