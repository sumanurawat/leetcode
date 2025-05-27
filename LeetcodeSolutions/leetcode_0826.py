class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        zipped_list = list(zip(difficulty, profit))
        zipped_list.sort()
        profits = [0] * len(profit)
        profits[0] = zipped_list[0][1]
        for i in range(1, len(zipped_list)):
            profits[i] = max(profits[i-1], zipped_list[i][1])
        
        worker.sort()

        ptr = 0
        result = 0
        for i in range(len(worker)):
            # if it's too difficult
            if worker[i] < zipped_list[ptr][0]:
                continue 
            # if it's doable, check if next one is also doable
            while ptr+1 < len(zipped_list) and zipped_list[ptr+1][0] <= worker[i]:
                ptr += 1
            result += profits[ptr]
        
        return result
