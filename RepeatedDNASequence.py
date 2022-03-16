from typing import List

'''
LeetCode 187
Repeated DNA Sequences
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seqmap = set()
        res = set()
        sarr = list(s)
        for i in range(len(sarr)):
            if i >= 9:
                if s[i-9:i+1] in seqmap:
                    res.add(s[i-9:i+1])
                else:
                    seqmap.add(s[i-9:i+1])
        
        return list(res)

sol = Solution()
print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(sol.findRepeatedDnaSequences("AAAAAAAAAAAAA"))