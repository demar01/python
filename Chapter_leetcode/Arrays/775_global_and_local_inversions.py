class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        N=len(A)
        for i in range(N):
            if abs(i - A[i]) > 1: return False
        return True