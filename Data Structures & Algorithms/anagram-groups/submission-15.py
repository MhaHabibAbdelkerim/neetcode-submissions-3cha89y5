class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_array = defaultdict(list)

        for string in strs:
            Count = [0] * 26
            
            for character in string:
                Count[ord(character) - ord("a")] += 1
            result_array[tuple(Count)].append(string)

        return list(result_array.values())