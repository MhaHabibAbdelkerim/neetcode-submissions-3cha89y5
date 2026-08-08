class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        L, R = 0, len(numbers) - 1
        while L <= R:
            TwoSum = numbers[L] + numbers[R]
            if TwoSum == target:
                return [L + 1, R + 1]
            elif TwoSum > target:
                R -= 1
            else:
                L += 1