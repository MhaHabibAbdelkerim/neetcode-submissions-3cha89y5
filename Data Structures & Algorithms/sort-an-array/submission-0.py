class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        middle = n // 2
        left_sorted = self.sortArray(nums[:middle])
        right_sorted = self.sortArray(nums[middle:])
        return self.merge(left_sorted, right_sorted)

    def merge(self, left_sorted, right_sorted):
        sorted = []
        i = j = 0
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] <= right_sorted[j]:
                sorted.append(left_sorted[i])
                i += 1
            else:
                sorted.append(right_sorted[j])
                j += 1

        sorted.extend(left_sorted[i:])
        sorted.extend(right_sorted[j:])

        return sorted