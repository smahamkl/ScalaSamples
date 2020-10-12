from typing import List
import collections
import itertools
'''
Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
Example 2:

Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
Example 3:

Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Constraints:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist of lowercase letters.
'''
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        i = 0
        j = len(A) - 1
        c1 = c2 = ''
        if len(A) != len(B) or (len(A) == len(B) == 0):
            return False
        if A == B:
            x = [item for item, count in collections.Counter(A).items() if count > 1]
            if len(x) > 0:
                return True
        while i < j:
            if A[i] == B[i]:
                i += 1
            elif A[j] == B[j]:
                j -= 1
            else:
                c1 = A[i]
                c2 = A[j]
                break
        if c1 == '' and c2 == '':
            return False
        
        if (A[:i] + c2 + A[i+1:j] + c1 + A[j+1:]) == B:
            return True
        
        return False
        

    
sol = Solution()
print(sol.buddyStrings("aaaaaaabc", "aaaaaaacb"))
print(sol.buddyStrings("abc", "cba"))
print(sol.buddyStrings("aaaaaaaa1", "aaaaaaaa2"))
print(sol.buddyStrings("abab", "abab"))
print(sol.buddyStrings("", "abab"))
print(sol.buddyStrings("abab", ""))
print(sol.buddyStrings("", ""))