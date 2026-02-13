'''
Question topic - String
Question link - https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
'''
# Sol -
# its not completed or correct
def sol(s):
    def is_pali(x):
        for i in range((len(x)//2)+1):
            if x[i] != x[-(i)]:
                return False
        return True
    #if is_pali(s):
    #    return 0
    dic = []
    for i in s:
        if i in dic:
            dic.remove(i) 
        else:
            dic.append(i)
    return len(dic) - 1

print(sol('no'))

