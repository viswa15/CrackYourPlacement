class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #depth first search to search the word in the board
        def search_word(x,y,idx):
            #check if last character matches
            if idx == len(word)-1:
                return board[x][y] == word[idx]

            # if current character does not match the word character at index,return False
            if board[x][y] != word[idx]:
                return False

            temp = board[x][y]
            board[x][y] = "0"
            #directions for exploring up,right,down,left
            directions = [(-1,0),(0,1),(1,0),(0,-1)]
            #loop through all possible directions
            for dx,dy in directions:
                new_x,new_y = x+dx,y+dy
                #check boundaries and if the next cell is not visited
                if 0 <= new_x < rows and 0 <= new_y < cols and board[new_x][new_y] != "0":
                    #recur the new position and the next character index
                    if (search_word(new_x,new_y,idx+1)):
                        return True

            #Restore the current cells value after exploring all directions
            board[x][y] = temp
            return False


        #retrieve the dimensions of the board
        rows,cols = len(board),len(board[0])
        #iterate through every charancter to match the first sequence
        for i in range(rows):
            for j in range(cols):
                #if first character matches then the word can be found there and return true
                if board[i][j] == word[0] and search_word(i,j,0):
                    return True

        #if the word can not be found return False
        return False
