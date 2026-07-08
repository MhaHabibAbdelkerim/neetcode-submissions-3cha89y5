class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        S = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[S] = nums[i]
                S += 1
        return S