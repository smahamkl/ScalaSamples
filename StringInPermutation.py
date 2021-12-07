from itertools import permutations

'''
Leetcode 567
https://leetcode.com/problems/permutation-in-string/

'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == None or s2 == None or len(s1) > len(s2):
            return False

        lookup1 = [ord(i) - ord('a') for i in s1]
        lookup2 = [ord(i) - ord('a') for i in s2]

        number1 = [0] * 26
        number2 = [0] * 26
        for i in lookup1:
            number1[i] +=1
    
        for i in range(len(s2)):
            number2[lookup2[i]] +=1

            if i >= len(s1):
                number2[lookup2[i- len(s1)]] -= 1
            
            if number1 == number2:
                return True

        
        return False

sol = Solution()
print(sol.checkInclusion('adc', "eidcaoook"))