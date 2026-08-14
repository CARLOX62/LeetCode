class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for ch in t:
            dic[ch] = dic.get(ch,0)+1
        for ch in s:
            dic[ch] -= 1
        for ch in dic:
            if dic[ch] > 0:
                return ch       