# Method: Use DFS to detect cycles in a directed graph using a hashmap (adjacency list)
# TC: O(V + E) where V is the number of courses and E is the number of prerequisites
# SC: O(V + E) for the hashmap and recursion stack

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Hashmap for <course: prerequisite[]>
        pre_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)

        # maintain currently visited nodes
        visited = set()

        def dfs(course):
            # visiting a node again / cycle detected
            if course in visited:
                return False

            visited.add(course)
            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            # mark the course as doable by removing prereqs
            pre_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
