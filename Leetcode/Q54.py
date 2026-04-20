'''
Question topic - Array
Question link - 
'''
# Sol - 
def spiralOrder(matrix):
    n = len(matrix)
    m = len(matrix[0])
    x,y = 0,0
    ans = []
    var = n*m
    while len(ans) < var:
        for j in range(y,m):
            ans.append(matrix[x][j])
        x += 1
        if len(ans) == var:
            break
        for i in range(x,n):
            ans.append(matrix[i][m-1])
        m -= 1
        if len(ans) == var:
            break
        for j in range(m-1,y-1,-1):
            ans.append(matrix[n-1][j])
        n -= 1
        if len(ans) == var:
            break
        for i in range(n-1,x-1,-1):
            ans.append(matrix[i][y])
        y += 1
        print(ans)
    return ans

print((spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])))