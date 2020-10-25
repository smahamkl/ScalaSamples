from typing import List
import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        while True:
            #---Alice is playing----
            possible_states_alice = []
            squared_steps = math.floor(n ** 0.5)
            possible_states_alice.append(n-1)
            #print("value of n:" + str(n))
            if n - (squared_steps ** 2) == 0:
                    return True
            while squared_steps >= 2:
                possible_states_alice.append(n - (squared_steps ** 2))
                squared_steps -= 1
            
            print(possible_states_alice)
            #---Alice is not playing---
            #--check if each of them is a winning state--
            #--return an optimal value-----
            #---probably an odd number
            alice_lost = True
            if len(possible_states_alice) == 1 and possible_states_alice[0] < 4:
                if possible_states_alice[0] % 2 == 0:
                    return True
                else:
                    return False
            for state in possible_states_alice:
                if (1 < state < 4 and state % 2 == 1):
                    alice_lost = False
                    n = state-1
                    break
                squared_steps = math.floor(state ** 0.5)
                while squared_steps >= 2: 
                    #print("squared steps:" + str(squared_steps))
                    if ((state - (squared_steps ** 2)) % 2) == 0:
                        n = state - (squared_steps ** 2)
                        alice_lost = False
                        break
                    squared_steps -= 1
                # if state % 2 == 1:
                #     alice_lost = False
                #     n = state-1
                #     break
                if not alice_lost:
                    break
            print("value of n after bob played:" + str(n))
            if alice_lost:
                return False
            
                

sol = Solution()
print(sol.winnerSquareGame(17))
# print(sol.winnerSquareGame(18))
#print(sol.winnerSquareGame(5))
#print(sol.winnerSquareGame(8))
#print(sol.winnerSquareGame(30))
#print(sol.winnerSquareGame(3))
#print(sol.winnerSquareGame(13))
