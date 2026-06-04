class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for n in strs:
            count = [0] * 26
            for c in n:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(n)
        return list(result.values())