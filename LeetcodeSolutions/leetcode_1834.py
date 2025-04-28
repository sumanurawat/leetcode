import heapq
from collections import deque
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # create a list of tasks in the order (start_time, duration, index) and sort it 
        task_list = []
        for i in range(len(tasks)):
            start_time = tasks[i][0]
            duration = tasks[i][1]
            index = i
            task_list.append((start_time, duration, index))
        task_list.sort()
        # task_list is a list of (start_time, duration, index) in order 
        result = []
        current_time = task_list[0][0]
        h = []
        task_list_idx = 0
        while len(result) < len(tasks):

            if len(h) == 0 and current_time < task_list[task_list_idx][0]:
                current_time = task_list[task_list_idx][0]
                
            while task_list_idx < len(task_list) and current_time >= task_list[task_list_idx][0]:
                start_time, duration, index = task_list[task_list_idx]
                heapq.heappush(h, (duration, index))
                task_list_idx += 1
            
            # now the heap has tasks that are waiting in line 
            # pick a task and complete it, move time forward and continue 
            duration, index = heapq.heappop(h)
            result.append(index)
            current_time += duration

        return result
