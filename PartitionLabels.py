import enum
from typing import List

'''
LeetCode 763
Partition Labels
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charmap = {0:0}
        res = []
            
        charmap = {chr:i for i,chr in enumerate(list(s))}

        j = anchor = 0

        for i, val in enumerate(s):
            j = max(j, charmap[s[i]])

            if i == j:
                res.append(i - anchor + 1)
                anchor = i+1
            
        return res

sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))
print(sol.partitionLabels("eccbbbbdec"))
print(sol.partitionLabels("e"))
print(sol.partitionLabels("caedbdedda"))
print(sol.partitionLabels("eaaaabaaec"))

