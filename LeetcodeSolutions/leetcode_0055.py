class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = 0
        for i in range(len(nums)):
            if can_reach < i:
                return False
            can_reach = max(can_reach, i+nums[i])
            if can_reach >= len(nums)-1:
                return True
        if can_reach < len(nums)-1:
            return False 
        return True