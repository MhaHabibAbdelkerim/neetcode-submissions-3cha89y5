class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Vote, Candidate = 0, 0

        for number in nums:
            if Vote == 0:
                Candidate = number
            Vote += (1 if number == Candidate else -1)

        return Candidate