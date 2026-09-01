class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        NumSet = set()
        for n in nums:
          if n in NumSet:
            return True
          NumSet.add(n)
        return False