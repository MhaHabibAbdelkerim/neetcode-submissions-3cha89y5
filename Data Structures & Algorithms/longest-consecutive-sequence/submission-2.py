class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in nums:
                counter = 0
                while n + counter in numset:
                    counter += 1
                longest = max(counter, longest)
        return longest