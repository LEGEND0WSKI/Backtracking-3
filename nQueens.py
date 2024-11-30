# // Time Complexity :O(n!*3n) for permutations and O(n) for safety
# // Space Complexity :O(n^2) for board, stack
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this :No 

# we need a Boolean Board to keep track of queens and recursion.
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        board = [[False] * n for _ in range(n)] #init board as False

        def helper(row,n):
            #base                               # make output
            if row == n:                        
                l1 = []
                for i in range(n):
                    l2 = ""
                    for j in range(n):
                        if board[i][j]:
                            l2+=("Q")
                        else:
                            l2+=(".")
                    l1.append(l2)
                result.append(l1)
                return

            #logic
            for j in range(n):                  # go over all columns
                if isSafe(board,row,j):         # diagonal and column ups have no queen?safe
                    board[row][j] = True        # action
                    helper(row+1,n)             # recursion
                    board[row][j] = False       # backtrack
                    
        def isSafe(board,i,j):                  # check all 3 directions north
            r,c = i,j
            while r >= 0:
                if board[r][c]  : return False
                r-=1

            r,c = i,j
            while r >= 0 and c >=0:
                if board[r][c]  : return False
                r-=1
                c-=1

            r,c = i,j
            while r >= 0 and c<n:
                if board[r][c]  : return False
                r -=1
                c +=1
   
            return True
        
        helper(0,n)
        return result