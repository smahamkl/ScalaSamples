'''
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement 
if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
Example 2:

Input: n = 1
Output: 1
'''
class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        def dfs(i, cands):
            if i <= 1:
                self.ans += 1
                return
            for j, x in enumerate(cands):
                if i % x == 0 or x % i == 0:
                    dfs(i-1, cands[:j] + cands[j+1:])
        dfs(n, list(range(1, n+1)))
        return self.ans
    
sol = Solution()
print(sol.countArrangement(5))