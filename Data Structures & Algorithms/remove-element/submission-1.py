class Solution:
    def removeElement(self, nums: List[t], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)