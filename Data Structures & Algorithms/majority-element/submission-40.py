class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        vote = 0
        for n in nums:
            if vote == 0:
                candidate = n
            vote += (1 if n == candidate else -1)
        return candidate