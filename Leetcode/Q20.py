'''
Question topic - string
Question link - https://leetcode.com/problems/valid-parentheses
'''
# Sol - 
def isValid(s: str) -> bool:
    stack = []
    dic = {')':'(','}':'{',']':'['}
    for x in s:
        if x in ['(','{','[']:
            stack.append(x)
        elif len(stack)==0 or dic[x] != stack.pop():
            return False
    if len(stack) != 0:
        return False
    return True