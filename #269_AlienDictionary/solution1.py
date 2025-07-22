# Method: Use Topological Sort (Postorder DFS) with Adjacency List
# Track visited and in-path nodes to detect cycles
# TC: O(N + V + E) where N is the number of words, V is the number of unique characters, and E is the number of edges
# SC: O(V + E) for the adjacency list and visited set
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Create Adjacency list
        adj = { c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # Visited=False; Path=True
        res = []

        # Post-order DFS Function
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)

        # Traverse Adj list, and call DFS
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)