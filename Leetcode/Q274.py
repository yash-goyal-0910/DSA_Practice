'''
Question topic - Array
Question link - 
'''
# Sol - 
def hIndex(citations):
    n = len(citations)
    ans = 0
    if n == 1:
        if citations[0] >= 1:
            return 1
        else:
            return 0
    citations = sorted(citations)
    for i,x in enumerate(citations):
        if n - i >= x:
            ans = x
            max_posi = n - i
        else:
            return min(ans,max_posi)
        
print(hIndex([4,0,6,1,4]))