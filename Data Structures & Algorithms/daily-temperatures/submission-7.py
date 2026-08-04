class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result_array = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                S_Temperature, S_Index = stack.pop()
                result_array[S_Index] = i - S_Index
            stack.append([t, i])

        return result_array