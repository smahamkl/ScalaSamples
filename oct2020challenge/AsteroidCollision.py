from typing import List
'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) == 0:
            return asteroids

        ast_stack = [asteroids[0]]
        for idx in range(1, len(asteroids)):
            if asteroids[idx] > 0 or len(ast_stack) == 0 or ast_stack[-1] < 0:
                ast_stack.append(asteroids[idx])
            elif asteroids[idx] < 0:
                winner = asteroids[idx]
                iterate = True
                while iterate:
                    if len(ast_stack) == 0 :
                        break
                    if (winner < 0 and ast_stack[-1] > 0):
                        ele = ast_stack.pop()
                        #print(winner, ele)
                        if winner + ele > 0:
                            ast_stack.append(ele)
                            iterate = False
                        elif winner + ele == 0:
                            iterate = False
                        elif (winner + ele) < 0 and len(ast_stack) == 0:
                            ast_stack.append(winner)
                            iterate = False
                    else:
                        ast_stack.append(winner)
                        iterate = False
        return ast_stack
sol = Solution()
print(sol.asteroidCollision([5,10,-5]))
print(sol.asteroidCollision([8,-8]))
print(sol.asteroidCollision([10,2,-5]))
print(sol.asteroidCollision([-2,-1,1,2]))
print(sol.asteroidCollision([-2,-2,1,-1]))
print(sol.asteroidCollision([1,-2,-2,-2]))
print(sol.asteroidCollision([1,-1,-1]))
print(sol.asteroidCollision([]))