class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        indices = []

        for i in range(m):
            for j in range(n):
                c = 0

                #top left
                if i > 0 and j > 0 and board[i-1][j-1] == 1:
                    c += 1

                #top
                if i > 0 and board[i-1][j] == 1:
                    c += 1

                #top right
                if i > 0 and j < n-1 and board[i-1][j+1] == 1:
                    c += 1

                #left
                if j > 0 and board[i][j-1] == 1:
                    c += 1

                #right
                if j < n-1 and board[i][j+1] == 1:
                    c += 1

                #bottom left
                if i < m-1 and j > 0 and board[i+1][j-1] == 1:
                    c += 1

                #bottom
                if i < m-1 and board[i+1][j] == 1:
                    c += 1

                #bottom right
                if i < m-1 and j < n-1 and board[i+1][j+1] == 1:
                    c += 1

                indices.append([board[i][j],c])

        for i in range(m):
            for j in range(n):
                cell = indices.pop(0)

                if cell[0] == 1:
                    if cell[1] < 2 or cell[1] > 3:
                        board[i][j] = 0
                elif cell[0] == 0 and cell[1] == 3:
                    board[i][j] = 1

