from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}
        incoming_count = {}

        for c2, c1 in prerequisites:
            if c1 not in adj_list:
                adj_list[c1] = []
            adj_list[c1].append(c2)

            if c2 not in incoming_count:
                incoming_count[c2] = 0
            incoming_count[c2] += 1

        order = []
        
        q = deque()

        for course in range(numCourses):
            if course not in incoming_count:
                q.append(course)

        while len(q) > 0:
            n = len(q)
            for i in range(n):
                current_course = q.popleft()
                order.append(current_course)
                
                # remove 1 incoming edge from all children, and if it's zero add to que 
                if current_course not in adj_list:
                    continue
                for child in adj_list[current_course]:

                    incoming_count[child] -= 1
                    if incoming_count[child] == 0:
                        q.append(child)
        if len(order) == numCourses:
            return order
        return []