class Solution:
    def calPoints(self, operations: List[str]) -> int:
        Result = []

        for ops in operations:
            if ops == "+":
                Result.append(Result[-1] + Result[-2])
            elif ops == "D":
                Result.append(Result[-1] * 2)
            elif ops == "C":
                Result.pop()
            else:
                Result.append(int(ops))
        
        return sum(Result)