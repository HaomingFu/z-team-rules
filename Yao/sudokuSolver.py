class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        if len(board)!= 9 or len(board[0])!=9:
            return
        self.solver(board, 0, 0)
        
    def solver(self, board, curLine, curRow):
        if curLine == 9:
            return
        if board[curLine][curRow]!='.':
            nextRow = 0 if curRow == 9 else curRow + 1
            nextLine = nextLine + 1 if curRow == 9 else nextLine
            self.solver(board, nextLine, nextRow)
            return
        for num in range(1,10):
            board[curLine][curRow]=num
            if self.isValid(board, curLine, curRow):
                nextRow = 0 if curRow == 9 else curRow + 1
                nextLine = nextLine + 1 if curRow == 9 else nextLine
                self.solver(board, nextLine, nextRow)
            board[curLine][curRow]='.'
    def isValid(self, board, curLine, curRow):
        for ix in range(9):
            if ix!=curRow and board[curLine][ix]==board[curLine][curRow]:
                return False
        for ix in range(9):
            if ix!=curLine and board[ix][curRow]==board[curLine][curRow]:
                return False
        ix = curLine / 3
        jx = curRow / 3
        for i in range(ix*3, 3*ix+3):
            for j in range(3*jx, 3*jx+3):
                if i!=curLine and j!=curRow and board[i][j] ==board[curLine][curRow]:
                    return False
                    
s = Solution()
board = [['.']*9 for i in range(9)]
s.solveSudoku(board)
print(board)
