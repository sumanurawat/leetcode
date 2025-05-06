class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mismatch_index = []
        if len(s1) != len(s2):
            return False 
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatch_index.append(i)
        if len(mismatch_index) == 0:
            return True
        if len(mismatch_index) == 1 or len(mismatch_index) > 2:
            return False
        
        if s1[mismatch_index[0]] == s2[mismatch_index[1]] and s1[mismatch_index[1]] == s2[mismatch_index[0]]:
            return True 
        return False