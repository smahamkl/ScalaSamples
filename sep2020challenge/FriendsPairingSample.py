import sys
'''
Friends Pairing Problem
18-02-2017
Given n friends, each one can remain single or can be paired up with some other friend. 
Each friend can be paired only once. 
Find out the total number of ways in which friends can remain single or can be paired up.

Examples :
Input  : n = 3
Output : 4
Explanation
{1}, {2}, {3} : all single
{1}, {2, 3} : 2 and 3 paired but 1 is single.
{1, 2}, {3} : 1 and 2 are paired but 3 is single.
{1, 3}, {2} : 1 and 3 are paired but 2 is single.
Note that {1, 2} and {2, 1} are considered same.
'''
def friendsPairs(n):
    dp = [0 for i in range(n+1)]
    for i in range(n + 1):
        if i <= 2:
           dp[i] = i
        else:
            dp[i] = dp[i-1] + (i-1) * dp[i-2]
    return dp[n]

if __name__ == "__main__":
    print(friendsPairs(5))
