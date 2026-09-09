class Solution:

    def encode(self, strs: List[str]) -> str:
        Result = []
        for s in strs:
            Result.append(str(len(s)))
            Result.append("@")
            Result.append(s)
        return "".join(Result)

    def decode(self, s: str) -> List[str]:
        Result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "@":
                j += 1
            Length = int(s[i:j])
            i = j + 1
            j = i + Length
            Result.append(s[i:j])
            i = j
        return Result