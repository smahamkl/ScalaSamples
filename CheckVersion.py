
from typing import List

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        res = 0

        strTok1 = version1.split(".")
        strTok2 = version2.split(".")
        minLen = min(len(strTok1), len(strTok2))
        maxLen = max(len(strTok1), len(strTok2))

        for i in range(maxLen):
            if i < minLen:
                if int(strTok1[i]) > int(strTok2[i]):
                    return 1
                elif int(strTok1[i]) < int(strTok2[i]):
                    return -1
            elif i >= minLen:
                if len(strTok1) > minLen:
                    if int(strTok1[i]) > 0:
                        return 1
                else:
                    if int(strTok2[i]) > 0:
                        return -1
        

        return res



if __name__ == "__main__":
    sol = Solution()
    print(sol.compareVersion("0.1", "1.1"))
    print(sol.compareVersion("1.0.1", "1"))
    print(sol.compareVersion("7.5.2.4", "7.5.3"))
    print(sol.compareVersion("1.01", "1.001"))
    print(sol.compareVersion("1.0", "1.0.0"))