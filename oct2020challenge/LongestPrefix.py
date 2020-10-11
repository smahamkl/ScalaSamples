from typing import List
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        prefix_map = {}
        if len(strs) == 0:
            return ""
        mlen = min([len(x) for x in strs])
        if mlen == 0:
            return ""
        for str in strs:
            head = prefix_map
            for char in str:
                if char not in prefix_map:
                    prefix_map[char] = {}
                prefix_map = prefix_map[char]
            prefix_map = head
        traverse = True
        while traverse and mlen > 0:
            if len(prefix_map.keys()) == 1:
                k = list(prefix_map.keys())[0]
                res += k
                prefix_map = prefix_map[k]
            else:
                traverse = False
            mlen -= 1
        
        return res

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dogw","dogwood","dogwear"]))
print(sol.longestCommonPrefix(["ab", "a"]))
print(sol.longestCommonPrefix(["ab", ""]))
print(sol.longestCommonPrefix([]))