class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        Result_array = [0] * len(temperatures)
        Stack = [] #[Temperature, Index]

        for index, temperature in enumerate(temperatures):
            while Stack and Stack[-1][0] < temperature:
                S_Temp, S_Index = Stack.pop()
                Result_array[S_Index] = index - S_Index
            Stack.append([temperature, index])
        
        return Result_array
