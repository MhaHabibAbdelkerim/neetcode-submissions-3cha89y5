class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
            length = len(nums)
            res = [0] * length

            for i in range(length):
                Product = 1
                for j in range(length):
                    if i == j:
                        continue
                    Product *= nums[j]
                res[i] = Product
            return res