class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_sorted = sorted(strs)
        first = str_sorted[0]
        last = str_sorted[-1]
        res = ''
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return res
            res+=first[i]
        return res
        