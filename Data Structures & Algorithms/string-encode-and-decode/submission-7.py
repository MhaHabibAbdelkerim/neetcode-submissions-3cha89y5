class Solution:

    def encode(self, strs: List[str]) -> str:
        result_array = []
        for string in strs:
            result_array.append(str(len(string)))
            result_array.append("#")
            result_array.append(string)
        return "".join(result_array)

    def decode(self, s: str) -> List[str]:
        Result_array = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            Length = int(s[i:j])
            i = j + 1
            j = i + Length
            Result_array.append(s[i:j])
            i = j
        
        return Result_array