'''
Question topic - String
Question link - https://leetcode.com/problems/repeated-string-match
'''
# Sol - 
def sol(a,b):
        val = 0
        if b == '':
            return val
        start = b.find(a)
        if start == -1:
            if a.find(b) != -1:
                return 1
            else:
                temp = a + a
                if temp.find(b) != -1:
                    return 2
            return -1
        ini = b[:start:]
        ini = ini[::-1]
        for i in range(len(ini)):
            if a[-(i+1)] != ini[i]:
                return -1
        b = b[start::]
        l_a = len(a)
        l_b = len(b)
        for i in range(l_b):
            if a[i%l_a] != b[i]:
                return -1
        val += l_b//l_a
        if l_b % l_a != 0:
            val += 1
        if start != 0:
            val += 1 
        return val