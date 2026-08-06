class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        j = 0
        n, m = len(word1), len(word2)
        while i < n and j < m:
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        result.extend(word1[i:])
        result.extend(word2[j:])
        return ''.join(result)