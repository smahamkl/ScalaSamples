from typing import List
import math
'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number 
of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.

Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
Example 4:

Input: n = 7
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 -> 0). 
If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 -> 0).
Example 5:

Input: n = 17
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
 

Constraints:

1 <= n <= 10^5
'''
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        square=[i**2 for i in range(1,int(n**0.5)+1)]
        print(square)
        dp=[False]*(n+1)
        for i in range(1,n+1):
        '''
        //as dp[i] is false, any square numbers from here onwards should return true,
        //so if dp[17] is false, dp[17+4], dp[17+9] and so on are true, as ALice can remove 4 and 9 from stones and return dp[17] to Bob and hence bob will fail
        '''
            for s in square:
                if s<=i:
                    if dp[i-s]==False:
                        dp[i]=True
                        break
                else:
                    break
        print(dp)
        return dp[-1]
        


sol = Solution()
print(sol.winnerSquareGame(49))
# print("------------------------")
# print(sol.winnerSquareGame(18))
# print("------------------------")
# print(sol.winnerSquareGame(5))
# print("------------------------")
#print(sol.winnerSquareGame(8))
# print("------------------------")
# print(sol.winnerSquareGame(30))
# print("------------------------")
# print(sol.winnerSquareGame(3))
# print("------------------------")
# print(sol.winnerSquareGame(13))
# print("------------------------")
# print(sol.winnerSquareGame(8))
# print("------------------------")
# print(sol.winnerSquareGame(1))
# print("------------------------")
# print(sol.winnerSquareGame(7))
# print("------------------------")
# print(sol.winnerSquareGame(15))
#print(sol.winnerSquareGame(47))
