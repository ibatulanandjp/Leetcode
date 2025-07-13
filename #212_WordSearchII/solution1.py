# Method: Use Trie to store words, and DFS to search for words in the board
# TC: O(N * M * 4^L), where N & M are the dimensions of the board, and L is the length of the longest word
# SC: O(W), where W is the total length of all words in the Trie
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
    
    def addWord(self, word: str):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create the Trie with words
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            # Base case
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            # Add the found word to the result
            if node.end_of_word:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))


        # DFS for each cell in the board to find word
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)