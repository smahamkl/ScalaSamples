from typing import List

'''
You have an initial power of P, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.

Example 1:

Input: tokens = [100], P = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.
Example 2:

Input: tokens = [100,200], P = 150
Output: 1
Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
There is no need to play the 1st token since you cannot play it face up to add to your score.
Example 3:

Input: tokens = [100,200,300,400], P = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:
1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.


I quick sort the tokens array in ascending order;
I iterate the arrays with two indices, left and right, proceeding depending on needs;
For each cycle I first check if there is enough power and I play face down if possible;
If there isn't enough power and score is >0 I play face up for increasing power;
For each cycle I can just play face up or down;
At each cycle I save the max Score;
If for a cycle I don't do any operation, end the cycle with a flag.
'''
class Solution:
    # def maxScore(self, arr:List[int], fdownIdx, P):
    #     P += arr[fdownIdx]
    #     score = 0
    #     for i in range(len(arr)):
    #         if i != fdownIdx:
    #             if P - arr[i] >= 0:
    #                 P-= arr[i]
    #                 score += 1
    #             else:
    #                 break
    #     return score

    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens)-1
        score = 0
        maxScore = 0
        flag = 1

        while l <= r and flag == 1:
            flag = 0
            if P >= tokens[l]:
                P -= tokens[l]
                l += 1
                score += 1
                flag = 1
            
            else:
                if score > 0:
                    P += tokens[r]
                    r -= 1
                    score -= 1
                    flag = 1
            maxScore = max(maxScore, score)
        
        return maxScore

#-----my work ----------------
    # def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
    #     if len(tokens) == 0:
    #         return 0
    #     elif len(tokens) == 1:
    #         return 1 if P >= tokens[0] else 0
        
    #     tokens = sorted(tokens)
    #     while True:
    #         #res = []
    #         score = 0
    #         sum = 0
    #         for i in range(len(tokens)):
    #             sum += tokens[i]
    #             if sum <= P:
    #                 #res.append(tokens[i])
    #                 score += 1
    #                 P = P - tokens[i]
    #             else:
    #                 if score >= 1 and i < len(tokens):
    #                     maxscore = score - 1
    #                     #newarr = [x for x in tokens if x not in res]
    #                     print(tokens[i:])
    #                     score -= 1
    #                     for j in  range(i, len(tokens)):
    #                         maxscore = max(maxscore, self.maxScore(tokens[i:], j-i, P))
    #                         print(maxscore, tokens[j], P)
    #                     score  = max(score+maxscore, score)
    #                     break
    #         print(score, P)
    #         break

sol = Solution()
print(sol.bagOfTokensScore([100,200,300,400], 200))