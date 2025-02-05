class Solution:
    def hammingWeight(self, n: int) -> int:
        steps = 0
        while n:
            if n & 1: steps += 1
            n = n >> 1
        return steps