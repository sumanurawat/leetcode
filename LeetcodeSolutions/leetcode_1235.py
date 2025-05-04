import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Create jobs as tuples and sort by start time
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        
        # DP array to store max profit at each index
        dp = [0] * n
        
        # Helper function to find next non-conflicting job
        def find_next_job(current_end_time, start_idx):
            # Find the first job that starts after current_end_time
            left, right = start_idx, n-1
            while left <= right:
                mid = (left + right) // 2
                if jobs[mid][0] >= current_end_time:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        # Fill dp array from right to left
        for i in range(n-1, -1, -1):
            # Take current job
            current_profit = jobs[i][2]
            next_job_idx = find_next_job(jobs[i][1], i+1)
            
            if next_job_idx < n:
                current_profit += dp[next_job_idx]
                
            # Don't take current job
            skip_profit = dp[i+1] if i+1 < n else 0
            
            dp[i] = max(current_profit, skip_profit)
        
        return dp[0] if n > 0 else 0
