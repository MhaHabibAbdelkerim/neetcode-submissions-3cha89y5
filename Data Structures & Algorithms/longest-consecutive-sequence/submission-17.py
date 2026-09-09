class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        NumSet = set(nums)
        LongestCS = 0

        for n in nums:
            if (n - 1) not in NumSet:
                Count = 1
                while (n + Count) in NumSet:
                    Count += 1
                LongestCS = max(LongestCS, Count)
            
        return LongestCS
