from itertools import combinations
from typing import List

class Solution:
    #---memory gettting exceeded----
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] ^ nums[0]
        elif len(nums) == 2:
            return nums[0] ^ nums[1]

        res =[x[0]^x[1] for x in list(combinations(nums, 2))]
        return max(res)



if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaximumXOR([3, 10, 5, 25, 2, 8]))
    
