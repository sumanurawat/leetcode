class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low = 1
        high = max(candies)

        def check_candies(candies_per_kid):
            total_kids = 0
            # can sort and break early here
            for i in range(len(candies)):
                total_kids += candies[i] // candies_per_kid

            if total_kids >= k:
                return True
            return False

        result = 0
        while low <= high:
            mid = (low + high) // 2

            if check_candies(mid):
                result = max(result, mid)
                low = mid + 1
            else:
                high = mid - 1
        return result
