class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        l = 0
        r = 0

        while l < n:
            if haystack[l] == needle[r]:
                l += 1
                r += 1

                if r == m:
                    return l - m
            else:
                l = l - r + 1
                r = 0
        return -1        