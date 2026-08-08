class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        HashSet = set()
        for number in nums:
          if number in HashSet:
            return True
          HashSet.add(number)

        return False