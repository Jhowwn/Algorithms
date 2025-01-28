class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, i in enumerate(nums):
            if d.get(i) is not None:
                return[d.get(i), idx]
            d[target-i] = idx      
        