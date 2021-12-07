from typing import List
'''
Leetcode - 49
https://leetcode.com/problems/group-anagrams/
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        ans = []
        for i in range(len(strs)):
            tmp = "".join(sorted(strs[i]))
            if tmp not in res:
                res[tmp] = [i]
            else:
                res[tmp].append(i)

        
        for v in res.values():
            ans.append([strs[x] for x in v])
        
        if len(ans) == 0:
            return [[""]]
        else:
            return ans


sol  = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams([""]))
print(sol.groupAnagrams(["a"]))