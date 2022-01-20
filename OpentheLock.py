from collections import deque
from operator import mod
from typing import List
from collections import deque
'''
LeetCode 752

Open the lock
https://www.youtube.com/watch?v=Pzg3bCDY87w
'''
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ulsteps = deque()
        ulsteps.append(["0000", 0])
        visited = set("0000")
        deadends = set(deadends)

        if target == "0000":
            return 0
        elif "0000" in deadends:
            return -1

        while ulsteps:
            tmp, totalmoves = ulsteps.popleft()
            
            for i in range(4):
                cur = int(tmp[i])
                if cur < 9 and cur > 0:
                    val1, val2 = cur + 1, cur - 1
                elif cur == 9:
                    val1, val2 = 0, cur - 1
                elif cur == 0:
                    val1, val2 = cur+1, 9
                
                str1 = tmp[:i] + str(val1) + tmp[i+1:]
                str2 = tmp[:i] + str(val2) + tmp[i+1:]

                #print(str1, str2, totalmoves)
                
                if str1 == target or str2 == target:
                    return totalmoves+1
                
                if str1 not in deadends and str1 not in visited:
                    ulsteps.append([str1, totalmoves+1])
                    visited.add(str1)
                
                if str2 not in deadends and str2 not in visited:
                    ulsteps.append([str2, totalmoves+1])
                    visited.add(str2)
        
        return -1


sol = Solution()
print(sol.openLock( ["0201","0101","0102","1212","2002"], "0202"))
print(sol.openLock( ["8888"], "0009"))
print(sol.openLock( ["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))
print(sol.openLock( ["0000"], "8888"))