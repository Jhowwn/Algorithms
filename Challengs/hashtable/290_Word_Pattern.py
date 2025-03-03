class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, map = s.split(' '), {}
        if len(pattern) != len(words): return False
        if len(set(pattern)) != len(set(words)): return False

        for i in range(len(words)):
            if words[i] not in map:
                map[words[i]] = pattern[i]
            elif map[words[i]] != pattern[i]:
                return False
        return True