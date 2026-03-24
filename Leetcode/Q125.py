'''
Question topic - Array
Question link - https://leetcode.com/problems/valid-palindrome
'''
# Sol - 
def isPalindrome(s: str) -> bool:
    n_s = ''
    for x in s:
        if x.isalpha():
            n_s += x.lower()
    if n_s == n_s[::-1]:
        return True
    return False

if isPalindrome("0P"):
    print('1')
else:
    print('0')