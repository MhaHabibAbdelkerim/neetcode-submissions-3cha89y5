class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result_array = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                STemperature, SIndex = stack.pop()
                result_array[SIndex] = i - SIndex
            stack.append([t, i])
        return result_array