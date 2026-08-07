class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        Window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                Window.remove(nums[L])
                L += 1
            if nums[R] in Window:
                return True
            Window.add(nums[R])

        return False