class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Nums1Index = {nums: i for i, nums in enumerate(nums1)}
        result_array = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                Value = stack.pop()
                Index = Nums1Index[Value]
                result_array[Index] = nums2[i]

            if nums2[i] in Nums1Index:
                stack.append(nums2[i])

        return result_array