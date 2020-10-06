from typing import List
import copy
from itertools import combinations
import re

class Solution:
    
    def lengthOfLastWord(self, s: str) -> int:
        if s is None:
            return 0
        s = re.sub(' +', ' ', s)
        strList = s.strip().split(' ')
        #strList = [lambda x: x.strip() for x in strList]
        print(strList)
        return len(strList[-1])



if __name__ == "__main__":
    sol = Solution()
    #print(sol.lengthOfLastWord("Hello World"))
    #print(sol.lengthOfLastWord("a"))
    print(sol.lengthOfLastWord("a "))