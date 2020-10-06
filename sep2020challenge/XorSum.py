from itertools import combinations
from typing import List

class Solution:
    #---not working yet solution
    def findMaximumXOR_1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] ^ nums[0]
        elif len(nums) == 2:
            return nums[0] ^ nums[1]

        maxL = len(bin(max(nums))[2:])
        bitArr:List[List[int]] = [[0 for x in range(maxL)] for x in range(len(nums))]

        groupA=[]
        groupB=[]
        groupC=[]
        groupD=[]

        for i in range(0, len(nums)):
            #binStr = bin(nums[i])[2:])
            #print(bin(nums[i])[2:])
            for j in range(maxL):
                if nums[i] & (1 << j):
                    bitArr[i][maxL -j -1] = 1
            
            if ((str(bitArr[i][0]) + str(bitArr[i][1])) == "10"):
                groupA.append(nums[i])
            elif ((str(bitArr[i][0]) + str(bitArr[i][1])) == "11"):
                groupB.append(nums[i])
            elif ((str(bitArr[i][0]) + str(bitArr[i][1])) == "01"):
                groupC.append(nums[i])
            else:
                groupD.append(nums[i])
        print(groupA)
        print(groupB)
        print(groupC)
        print(groupD)
    def findMaximumXOR(self, nums: List[int]) -> int:
        bin_list = ["{0:b}".format(el) for el in nums]
        max_len = len(max(bin_list, key = lambda x: len(x)))
        bin_list = ["0"*(max_len - len(el)) + el for el in bin_list]
        print(bin_list)
        ans = float('-inf')
        # create a trie and for each representation try to find the exact opposite as much as possible
        trie = {}
        for word in bin_list:
            parent = trie
            for char in (word):
                if char in parent:
                    parent = parent[char]
                else:
                    parent[char] = {}
                    parent = parent[char]
        print(trie)
        print(parent)
        # now for each item in binary_list, try to find the opposite
        ans = float('-inf')
        for word in bin_list:
            parent = trie
            curr = ''
            for idx, char in enumerate(word):
                to_find = '1' if char == '0' else '0'
                if to_find in parent:
                    curr += to_find
                    parent = parent[to_find]
                else:
                    curr += char
                    parent = parent[char]
                if idx == len(word) - 1:
                    ans = max(ans, int(word, 2) ^ int(curr, 2) )
        return ans 




if __name__ == "__main__":
    sol = Solution()
    #print(sol.findMaximumXOR([3, 10, 5, 25, 2, 8]))
    print(sol.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))
