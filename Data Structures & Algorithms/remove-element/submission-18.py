class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        for n in nums:
            if n != val:
                nums[L] = n
                L += 1
        return L