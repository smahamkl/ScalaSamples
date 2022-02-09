# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    n = 9
    if num == n:
        return 0
    elif num < n:
        return 1
    else:
        return -1

class Solution:
    def guessNumber(self, n: int) -> int:
        st,end = 1,n
        while st < end:
            #print(st, end)
            if guess(st) == 0:
                return st
            elif guess(end) == n:
                return end
            mid = (st+end) // 2
            res = guess(mid)
            if res == -1:
                st = 1
                end = mid-1
            elif res:
                st = mid + 1
            else:
                return mid
        return st

sol = Solution()
print(sol.guessNumber(2**30))

