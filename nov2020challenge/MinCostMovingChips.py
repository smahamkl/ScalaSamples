from typing import List
from queue import PriorityQueue
import collections
'''
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.

 
Example 1:


Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.
'''
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        #---idea is to bring all chips to one of the two positions (position % 2) since 
        #---switching cost for two positions is 0, and then finally taking the minimum
        #---count of chips from each of the positions
        num_map = {x:cnt for x,cnt in collections.Counter([x%2 for x in position]).items()}
        if len(num_map.keys()) == 1:
            return 0
        else:
            return min(num_map.values())

sol = Solution()
print(sol.minCostToMoveChips([2]))
print(sol.minCostToMoveChips([2,2,2,3,3,4,4,4]))
print(sol.minCostToMoveChips([1,1000000000]))
print(sol.minCostToMoveChips([1,2,3]))
print(sol.minCostToMoveChips([2,2,2,2,2,2,2]))