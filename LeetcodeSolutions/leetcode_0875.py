class Solution:
    def possible(self, eat_rate, hours, piles):
        current_hours = 0
        for pile in piles:
            current_hours += math.ceil(pile/eat_rate)
            if current_hours > hours:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        result = right
        while left <= right:
            mid = (right + left) // 2
            if self.possible(mid, h, piles):
                result = min(result, mid)
                right = mid-1
            else:
                left = mid+1
        return result
