class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        map = {}

        for i in magazine:
            map[i] = map.get(i, 0) + 1
        
        for j in ransomNote:
            if j not in map or map[j] == 0:
                return False
            map[j] -= 1
        return True