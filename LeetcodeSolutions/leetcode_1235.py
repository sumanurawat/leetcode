import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Create jobs as tuples and sort by start time
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        n = len(jobs)
        
        # Extract start times for binary search
        start_times = [job[0] for job in jobs]
        
        # DP array to store max profit at each index
        dp = [0] * n
        
        # Fill dp array from right to left
        for i in range(n-1, -1, -1):
            # Take current job
            current_profit = jobs[i][2]
            
            # Find next non-conflicting job using bisect
            next_job_idx = bisect.bisect_left(start_times, jobs[i][1], i+1)
            
            if next_job_idx < n:
                current_profit += dp[next_job_idx]
                
            # Don't take current job
            skip_profit = dp[i+1] if i+1 < n else 0
            
            dp[i] = max(current_profit, skip_profit)
        
        return dp[0] if n > 0 else 0
