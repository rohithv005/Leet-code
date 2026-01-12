class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)

            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)

        return list(anagrams.values())
