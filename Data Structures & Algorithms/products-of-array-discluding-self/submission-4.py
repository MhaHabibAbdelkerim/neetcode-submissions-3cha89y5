class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
            length = len(nums)
            result_array = [0] * length

            for i in range(length):
                Product = 1
                for j in range(length):
                    if i == j:
                        continue
                    Product *= nums[j]
                result_array[i] = Product
            return result_array