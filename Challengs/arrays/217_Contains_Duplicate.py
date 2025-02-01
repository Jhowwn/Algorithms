# Solution using Hash Map
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         map = {}
        
#         for num in nums:
#             if num in map and map[num] >= 1:
#                 return True
#             map[num] = map.get(num, 0) + 1
#         return False

# Solution using Set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nset = set()
        for num in nums:
            if num in nset:
                return True
            else:
                nset.add(num)
        return False