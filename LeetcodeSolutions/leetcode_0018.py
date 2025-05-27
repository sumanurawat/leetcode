class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        m = {}
        nums.sort()
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = []
            m[nums[i]].append(i)
        result = set()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    rem = target - nums[i] - nums[j] - nums[k]
                    if rem in m:
                        for idx in m[rem]:
                            if idx > k:
                                result.add((nums[i], nums[j], nums[k], nums[idx]))
        return list(x for x in result)
