import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] *= -1
        heapq.heapify(nums)
        current_sum = total
        operations = 0
        while current_sum > total/2:
            operations += 1
            max_num = -heapq.heappop(nums)
            current_sum -= max_num/2
            heapq.heappush(nums, -max_num/2)
        return operations