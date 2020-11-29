from typing import List
from collections import Counter

'''
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
'''

class Solution:
    def longestSubstring(self, s, k):
        def divide_and_conquer(s):
            
            char_freq = Counter(s)
            
            for i, c in enumerate(s):
                
                if char_freq[c] < k:
                    
                    j = i + 1
                    while j < len(s) - 1 and char_freq[s[j]] < k:
                        j += 1
                        
                    return max(divide_and_conquer(s[:i]), divide_and_conquer(s[j:]))
                        
            return len(s)
              
        return divide_and_conquer(s)

sol = Solution()
print(sol.longestSubstring("aaabb", 3))
print(sol.longestSubstring("ababbc", 2))