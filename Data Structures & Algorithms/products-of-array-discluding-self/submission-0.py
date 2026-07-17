class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
            result_array = [0] * len(nums)
            for i in range(len(nums)):
                if i == 0:
                    Product = 1
                    for j in range(i + 1, len(nums)):
                        Product = Product * nums[j]
                    result_array[i] = Product
                Left_Product = nums[:i]
                Right_Product = nums[i + 1:]
                L, R = 1, 1
                for w in range(len(Left_Product)):
                    L = L * Left_Product[w]
                for j in range(len(Right_Product)):
                    R = R * Right_Product[j]
                result_array[i] = L * R
            return result_array