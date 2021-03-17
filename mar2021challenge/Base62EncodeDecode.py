
class Solution:
    def __init__(self):
        self.chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def mod36encode(self, a:int) -> str:
        res = ""
        while True:
            res += self.chrs[a % 52]
            a = int(a / 52)
            if a == 0:
                break
        return res[::-1]
    
    def mod36decode(self, url) -> int:
        res = 0
        idx = 0
        for i in range(len(url)-1,-1, -1):
            res += self.chrs.index(url[i]) * (52 ** idx)
            idx += 1
        
        return res

sol = Solution()
encdstr = sol.mod36encode(1234123567)
print(encdstr)
decdstr = sol.mod36decode(encdstr)
print(decdstr)