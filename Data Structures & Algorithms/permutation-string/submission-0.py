class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        CountS1 = {}
        Count = {}
        L = 0

        for i in range(len(s1)):
            CountS1[s1[i]] = 1 + CountS1.get(s1[i], 0)

        for R in range(len(s2)):
            Count[s2[R]] = 1 + Count.get(s2[R], 0)
            while (R - L + 1) > len(s1):
                Count[s2[L]] -= 1

                if Count[s2[L]] == 0:
                    del Count[s2[L]]
                L += 1
            
            if Count == CountS1:
                return True
            
        return False