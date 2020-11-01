from typing import List
'''
Number of longest increasing subsequences inside an array
'''
class Solution:
    #-----method I tried - recursive
    # def __init__(self):
    #     self.res = []
    # def LIS(self, nums:List[int], seq:List[int], cur_idx:int):
    #     if cur_idx < len(nums):
    #         l1 = l2 = None
    #         if nums[cur_idx] > seq[-1]:
    #             l1 = self.LIS(nums, seq + [nums[cur_idx]], cur_idx+1)
    #             l2 = self.LIS(nums, seq, cur_idx+1)
    #         else:
    #             l1 = self.LIS(nums, seq, cur_idx+1)
    #             l2 = self.LIS(nums, [nums[cur_idx]], cur_idx+1)
    #         if cur_idx + 1 == len(nums):
    #             if len(l1) > len(l2):
    #                 self.res += [l1]
    #             elif len(l2) > len(l1):
    #                 self.res += [l2]
    #     else:
    #         return seq

    # def findNumberOfLIS1(self, nums: List[int]) -> int:
    #     if len(nums) <= 1:
    #         return len(nums)
    #     self.LIS(nums,[nums[0]], 1)
    #     print(self.res)
    #     if len(self.res) == 0:
    #         return len(nums)
    #     self.res = sorted(self.res, reverse=True, key=lambda x:len(x))
    #     lis = [x for x in self.res if len(x) == len(self.res[0])]
    #     return len(lis)
    '''
    Dynamic programming. Current state is stored in array data structure, indexed by sequence length, and updated as we read each value in nums. 
    Each element of the array at index j contains two elements: [int, dict]. The integer is the smallest terminal value available for an existing 
    sequence of length = array index. The dict within index j contains all terminal values of j-length subseqs that may still be relevant for future extensions.

For each new value n in nums, find the longest possible sequence length j that terminates at value n by binary search over the int entries. Any (j-1)-length 
subseqs terminating at a greater or equal value are now superseded, so remove them from the dict at index j-1. Compute number of j-length paths terminating 
at n by summing over the remaining values in the dict at j-1.

Also there is a detailed explanation documented on google drive


    '''
    def findNumberOfLIS(self, nums: List[int]) -> int:
        def binary_search(k):
            (a,b)=(-1,len(data))
            while((b-a)>1):
                piv=(a+b)//2
                if (n<=data[piv][0]):
                    b=piv
                else:
                    a=piv
            return(a)
        
        big=1111111
        data=[[-big,{-big:1}]]
        # data[j]=== [minEndVal,{v:multiplicity for v in endvals}]
        for n in nums:
            new_len = binary_search(n)+1
            keylist = list(data[new_len-1][1].keys())
            for key in keylist:
                if (key>=n):
                    del data[new_len-1][1][key]
            if (new_len==len(data)):
                data.append([n,{n:sum(data[-1][1].values())}])
            else:
                data[new_len][1][n] = data[new_len][1].get(n,0) + sum(data[new_len-1][1].values())
                data[new_len][0] = min(n,data[new_len][0])
            print("value of n:", n, " new_length value:",  new_len)
            print(data)
        return(sum(data[-1][1].values()) if nums else 0)

        
sol = Solution()
print(sol.findNumberOfLIS([1,3,5,4,2,7,6]))
#print(sol.findNumberOfLIS([2,2,2,2,2]))
#print(sol.findNumberOfLIS([1,4,4,4]))
#print(sol.findNumberOfLIS([1,2,4,3,5,4,7,2]))
#print(sol.findNumberOfLIS([1,1,1,2,2,2,3,3,3]))