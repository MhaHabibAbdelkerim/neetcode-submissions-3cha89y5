class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, votes = 0, 0

        for n in nums:
            if votes == 0:
                candidate = n
            votes += (1 if n == candidate else -1)
        return candidate
            