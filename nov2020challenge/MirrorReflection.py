from typing import List
'''
There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

 

Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

Solution:
---------
During each horizontal traversal (from left to right or from right to left), the total vertical distance covered is (q/p). To reach a receptor, 
we require the total distance both horizontal and vertical to an integer multiple of p. Hence we seek the smallest positive integer multiple of (q/p) that is itself an integer.

This boils down to expressing (q/p) as a reduced fraction. Further, since we only care about even vs odd, we only need to reduce the fraction by mutual multiples of 2.

The destination receptor will depend on the even-odd parity of the reduced p and q as follows: (Even p and odd q => receptor 2, Odd p and odd q => receptor 1, Odd p and even q => receptor 0).

Another solution with explanation:
https://leetcode.com/problems/mirror-reflection/discuss/939286/Mirror-Mirror-Flip-Flip-with-Pictures-%2B-10-lines-of-code-EVERYONE-CAN-UNDERSTAND!-YOU-TOO!
'''

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while (not((p%2)or(q%2))):
            (p,q) = (p//2,q//2)
        return(1+(q%2)-(p%2))

sol = Solution()
print(sol.mirrorReflection(2,1))