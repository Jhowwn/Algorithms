class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(numbers):
            if target - num in d:
                return[d[target-num]+1, idx+1]
            d[num] = idx