'''
Question topic - Array
Question link - 
'''
# Sol - 
def threeSum(nums: list[int]) -> list[list[int]]:
    n,z,p = [],[],[]
    for i in range(len(nums)):
        x = nums[i]
        if x < 0:
            n.append(x)
        elif x > 0:
            p.append(x)
        else:
            z.append(x)
    N = set(n)
    P = set(p)
    s = set()
    
    if len(z) >= 3:
        s.add((0,0,0))
    
    if z:
        for n_no in N:
            fn = n_no * -1
            if fn in P:
                s.add((n_no , 0, fn))
    
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            m = -1 * (n[i] + n[j])
            if m in P:
                s.add(tuple(sorted([n[i],n[j],m])))
    
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            m = -1 * (p[i] + p[j])
            if m in N:
                s.add(tuple(sorted([p[i],p[j],m])))
    return list(s)