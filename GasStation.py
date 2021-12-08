from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            if gas[0] - cost[0] >= 0: return 0
            else: return -1
            
        gas_rearr = [x for x in gas] * 2
        cost_rearr = [x for x in cost] * 2

        travel_arr = [gas_rearr[i] - cost_rearr[i] for i in range(len(gas_rearr))]

        print(travel_arr)

        for i in range(len(gas)):
            if travel_arr[i] > 0:
                bal = 0 
                for j in range(len(gas)):
                    bal += travel_arr[i+j]
                    if bal < 0:
                        break
                if bal >= 0:
                    return i
        return -1


sol = Solution()
print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))