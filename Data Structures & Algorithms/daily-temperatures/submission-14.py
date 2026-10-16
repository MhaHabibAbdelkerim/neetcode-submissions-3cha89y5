class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result_array = [0] * len(temperatures)
        stack = [] #Pair: [temp, index]

        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                TEMP, INDEX = stack.pop()
                result_array[INDEX] = index - INDEX
            stack.append([temperature, index])

        return result_array