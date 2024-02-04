class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        resultIndices, windowStart, matched = [], 0, 0
        characters = {}
        for i in range(len(p)): characters[p[i]] = characters.get(p[i], 0) + 1

        for windowEnd in range(0, len(s)):
            if s[windowEnd] in characters:
                characters[s[windowEnd]] -= 1
                if characters[s[windowEnd]] == 0: matched += 1
            
            if matched == len(characters): resultIndices.append(windowStart)

            if windowEnd >= len(p) - 1:
                if s[windowStart] in characters:
                    if characters[s[windowStart]] == 0: matched -= 1
                    characters[s[windowStart]] += 1
                windowStart += 1

        return resultIndices
