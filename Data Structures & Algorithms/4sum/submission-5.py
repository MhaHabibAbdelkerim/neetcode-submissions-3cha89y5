class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                L, R = j + 1, len(nums) - 1
                while L < R:
                    total = nums[i] + nums[j] + nums[L] + nums[R]
                    if total > target:
                        R -= 1
                    elif total < target:
                        L += 1
                    else:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        L += 1
                        R -= 1

                        while L < R and nums[L] == nums[L - 1]:
                            L += 1
                        while L < R and nums[R] == nums[R + 1]:
                            R -= 1
        return res