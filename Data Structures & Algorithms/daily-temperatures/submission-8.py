class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result_array = [0] * len(temperatures)
        stack = [] # Stores [temperature, Index]

        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                S_Temperature, S_Index = stack.pop()
                result_array[S_Index] = index - S_Index
            stack.append([temperature, index])

        return result_array