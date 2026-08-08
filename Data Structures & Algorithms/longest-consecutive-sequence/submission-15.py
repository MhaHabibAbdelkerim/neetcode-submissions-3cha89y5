class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Longest_C_Sequence = 0
        HashSet = set(nums)

        for number in nums:
            if (number - 1) not in HashSet:
                Count = 0
                while (number + Count) in HashSet:
                    Count += 1
                Longest_C_Sequence = max(Longest_C_Sequence, Count)

        return Longest_C_Sequence