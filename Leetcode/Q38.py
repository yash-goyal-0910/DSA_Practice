'''
Question topic - String
Question link - https://leetcode.com/problems/count-and-say/
'''
# Sol - 
def count_say(n):
    if n == 1:
        return '1'
    st = count_say(n-1)
    out = []
    time = 0
    prev = ''
    for i,x in enumerate(st):
        if x == prev:
            time += 1
        else:
            if prev == '':
                time += 1
                prev = x
            else:
                out.append(f"{time}{prev}")
                time = 1
                prev = x
    out.append(f"{time}{prev}")
    return ''.join(out)
