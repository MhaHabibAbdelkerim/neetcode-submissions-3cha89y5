class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        res = set(nums)
        
        for n in nums:
            if n - 1 not in res:
                count = 0
                while (n + count) in res:
                    count += 1
                longest = max(longest, count)
        return longest

