'''
Question topic - Array
Question link - https://leetcode.com/problems/integer-to-roman
'''
# Sol - 
def intToRoman(num: int) -> str:
    ans = []
    def val_t(x):
        if x == 1:
            return 'I'
        if x == 5:
            return 'V'
        if x == 10:
            return 'X'
        if x == 50:
            return 'L'
        if x == 100:
            return 'C'
        if x == 500:
            return 'D'
        if x == 1000:
            return 'M'

    num_s = str(num)
    n = 10**len(num_s)
    for i in num_s:
        i = int(i)
        n = n//10
        if i == 4 or i == 9:
            ans.append(1*(n))
            ans.append((i+1)*(n))
        elif i>0 and i<4:
            for x in range(i):
                ans.append(1*(n))
        elif i>4:
            ans.append(5*(n))
            for x in range(5,i):
                ans.append(1*(n))

    for i,x in enumerate(ans):
        s = val_t(x)
        ans[i] = s

    return ''.join(ans)

print(intToRoman(299))