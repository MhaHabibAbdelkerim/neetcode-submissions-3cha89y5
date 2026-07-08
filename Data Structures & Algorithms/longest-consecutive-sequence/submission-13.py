class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        reference = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in reference:
                count = 0
                while (n + count) in reference:
                    count += 1
                longest = max(count, longest)
        
        return longest