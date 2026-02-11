'''
Question topic - String
Question link - https://leetcode.com/problems/repeated-string-match
'''
# Sol - 
def sol(a,b):
    l_b = len(b)
    temp = a
    if l_b == 0:
        return 0
    l_a = len(a)
    time = 1
    while len(a)//l_b < 1:
        time += 1
        a += temp
    if a.find(b) == -1:
        time += 1
        a += temp
    if a.find(b) == -1:
        time += 1
        a += temp
    if a.find(b) == -1:
        return -1        
    return time

print(sol("abc","cabcabca"))