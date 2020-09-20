from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digitySeq="123456789"
        l = len(str(low))
        r = len(str(high))
        res = []
        for i in range(l, r+1):
            for j in range(len(digitySeq)-i+1):
                num = int(digitySeq[j:i+j])
                if (num >= low) and (num <= high):
                    res.append(num)

        return res
        

sol = Solution()
print(sol.sequentialDigits(100,300))
print(sol.sequentialDigits(1000,13000))
print(sol.sequentialDigits(10,10))