'''
Question topic - Array
Question link - 
'''
# Sol - 
def isValidSudoku(board: List[List[str]]) -> bool:
    for x in range(9):
        ls = [0]*9
        for y in range(9):
            temp = board[x][y]
            if temp == '.':
                continue
            ls[(int(temp)-1)] += 1
            if ls[(int(temp)-1)] > 1:
                return False
    for x in range(9):
        ls = [0]*9
        for y in range(9):
            temp = board[y][x]
            if temp == '.':
                continue
            ls[(int(temp)-1)] += 1
            if ls[(int(temp)-1)] > 1:
                return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            ls = [0]*9
            for y in range(3):
                for z in range(3):
                    temp = board[i+y][j+z]
                    if temp == '.':
                        continue
                    ls[(int(temp)-1)] += 1
                    if ls[(int(temp)-1)] > 1:
                        return False
    return True     

print(isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]))