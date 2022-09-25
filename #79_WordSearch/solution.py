from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        # path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r<0 or r>=rows or 
                c<0 or c>=cols or
                word[i] != board[r][c]):
                # or (r, c) in path):
                return False
            
            # path.add((r,c))
            temp = board[r][c]
            board[r][c] = "#"
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            # path.remove((r,c))
            board[r][c] = temp
            
            return res        
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0): return True #(row, col, word_index)
        return False