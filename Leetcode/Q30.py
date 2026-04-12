'''
Question topic - Sliding Window
Question link - https://leetcode.com/problems/substring-with-concatenation-of-all-words/
'''
# Sol - 
def findSubstring(s: str, words: List[str]) -> List[int]:
    l = len(words[0])
    n = len(words)
    dic = dict()
    for x in words:
        if x in dic:
            dic[x] -= 1
        else:
            dic[x] = 0
    ans = []
    i = 0
    while i <= (len(s)-(l*n)): 
        word = s[i:i+(l*n):]
        if word[:l] in words:
            j = 0
            temp_d = dict(dic)
            while j < (l*n):
                temp = word[j:j+l]
                if temp not in dic:
                    break
                else:
                    temp_d[temp] += 1
                    if temp_d[temp] > 1:
                        break
                    elif j == (n*l)-l:
                        ans.append(i)
                j += l
        i += 1
    return ans

print(findSubstring("barfoothefoobarman",["foo","bar"]))