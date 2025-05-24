from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjacency list to represent the graph
        adj_list = {}
        # Dictionary to keep track of in-degrees (number of prerequisites) for each course
        in_degree = {}
        for second, first in prerequisites:
            # Add an edge from 'first' to 'second' in the adjacency list
            if first not in adj_list:
                adj_list[first] = set()
            adj_list[first].add(second)   

            # Update the in-degree for the 'second' course
            if second not in in_degree:
                in_degree[second] = 0
            in_degree[second] += 1

        # Set to keep track of courses that have been visited (taken)
        visited = set()
        # Queue for BFS; start with courses that have no prerequisites (in-degree 0)
        q = deque()
        for n in range(numCourses):
            if n not in in_degree:
                q.append(n)
        
        # Process courses in BFS order
        while len(q) > 0:
            top = q.pop()
            visited.add(top)
            # If this course has no dependents, continue
            if top not in adj_list:
                continue
            # For each course that depends on 'top'
            for node in adj_list[top]:
                # Decrement in-degree for each dependent course
                if node in in_degree and in_degree[node] > 0:
                    in_degree[node] -= 1
                # If in-degree becomes 0 and not yet visited, add to queue
                if node not in visited and in_degree[node] == 0:
                    q.append(node)
        # If all courses are visited, return True; otherwise, False
        return len(visited) == numCourses

# Time Complexity: O(N + E), where N = numCourses and E = number of prerequisites.
#   - Building the graph and in-degree dict takes O(E).
#   - Each course is processed at most once (O(N)).
#   - For each course, we process all its dependents (O(E) in total).
# Space Complexity: O(N + E) for the adjacency list, in-degree dict, visited set, and queue.
