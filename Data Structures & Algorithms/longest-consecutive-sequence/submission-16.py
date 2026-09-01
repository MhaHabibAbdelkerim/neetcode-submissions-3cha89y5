class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        NumSet = set(nums)
        LongestCSeq = 0

        for n in nums:
            if (n - 1) not in NumSet:
                Count = 0
                while (n + Count) in NumSet:
                    Count += 1
                LongestCSeq = max(LongestCSeq, Count)
        return LongestCSeq