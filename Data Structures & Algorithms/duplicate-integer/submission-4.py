class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for i, n in enumerate(nums):
            if n in seen:
                return True
            else:
                seen[n] = i
        return False