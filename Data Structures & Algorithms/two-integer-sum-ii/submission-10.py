class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            Sum = numbers[L] + numbers[R]
            if Sum > target:
                R = R - 1
            elif Sum < target:
                L = L + 1
            else:
                return [L + 1, R + 1]