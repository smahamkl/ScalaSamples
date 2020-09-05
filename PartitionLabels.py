from typing import List

'''
Leet code Sep 2020 Challenge
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
'''
class Solution:

    def partitionLabels(self, S: str) -> List[int]:

        partDict = {x: '' for x in range(len(S))} 
        partDict1 = {}

        for idx, char in enumerate(S):
            partDict[ord(char) - ord('a')]  += str(idx) + ":"
        
        for key in partDict:
            if partDict[key] != '':
                val = list(filter(None, partDict[key].split(":")))
                partDict1[int(val[0])] = int(val[len(val) - 1])
        #print(self.partDict1)
        res = []
        
        tempKey = next(iter(sorted(partDict1)))
        tempVal = partDict1[tempKey]

        for key in sorted(partDict1):
            if (key <= tempVal) & (partDict1[key] > tempVal):
                 tempVal = partDict1[key]
            elif key > tempVal:
                res.append(tempVal - tempKey + 1)
                tempKey = key
                tempVal = partDict1[key]
            #print("key value: " + str(tempKey) + " temp val: " + str(tempVal))
        
        res.append(len(S) - sum(res))
        
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.partitionLabels("ababcbacadefegdehijhklij"))
    print(sol.partitionLabels("dccccbaabe"))