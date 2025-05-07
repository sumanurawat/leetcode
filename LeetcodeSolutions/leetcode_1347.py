class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = {}
        result = 0
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        for c in t:
            if c in freq and freq[c] > 0:
                freq[c] -= 1
            else:
                result += 1
        return result