
from itertools import permutations 
'''
Given an array of 4 digits, return the largest 24 hour time that can be made
The smallest 24 hour time is 00:00, and the largest is 23:59
Starting from 00:00, a time is larger if more time has elapsed since midnight
Return the answer as a string of length 5.  If no valid time can be made, return an empty string

Example 1:
Input: [1,2,3,4]
Output: "23:41"

Example 2:
Input: [5,5,5,5]
Output: ""
'''
class Solution:

    def __init__(self):
        self.maxHour = "-1"

    def max(self, a, b):
        if(int(a) > int(b)):
            return a
        else:
            return b
    def getParsedHr(self, a: str) -> str:
        return a[0] + a[1] +":" + a[2] + a[3]

    def isValidTime(self, hr, min)->bool:
        if((hr < 24) & (min < 60)):
            return True
        else:
            return False

    def largestTimeFromDigits(self, A) -> str:
        perm = permutations(A, 4)
        for i in list(perm): 
            #print(int(str(i[0]) + str(i[1])),  int(str(i[2]) + str(i[3])))
            if(self.isValidTime( int(str(i[0]) + str(i[1])),  int(str(i[2]) + str(i[3])) )):
                self.maxHour = self.max(''.join(map(str, i)), self.maxHour)
                print(i)
        if self.maxHour == "-1":
            return ""
        else:
            return self.getParsedHr(self.maxHour)

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestTimeFromDigits([5,5,5,5]))
