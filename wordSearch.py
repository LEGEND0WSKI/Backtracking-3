# // Time Complexity :O(m*n*4^k) k = wordsze//every item is traversed in 4 directions
# // Space Complexity :O(k) for recursion stack
# // Did this code successfully run on Leetcode: Yes
# // Any problem you faced while coding this : Nonlocal flag, op condition before boundary, main function dfs break condition, too much runtime

class Solution:     
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        flag = False

        def dfs(board,i,j,word,idx):

            nonlocal flag                                               # nonglobal nonlocal variable
            #base
            if idx == len(word):                                        #check if word found first
                flag = True 
                return

            if i<0 or i==m or j < 0 or j == n or board[i][j] == "#":    #then check boundaries
                return
        
            #logic
            if board[i][j] == word[idx]:
                board[i][j] = '#'                   #action

                for di in dirs:                     #recursion x4
                    r = di[0] +i
                    c = di[1] +j
                    dfs(board,r,c,word,idx+1)

                board[i][j] = word[idx]             #backtrack

        for i in range(m):                                              # build output
            for j in range(n):
                    if board[i][j] == word[0]:      # if first letter of word is found(start recursion)
                        if dfs(board,i,j,word,0):   # dfs becomes true? exit early
                            break

        return flag

arr = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
w = "SEEK"

x = Solution().exist(arr,w)
print(x)
