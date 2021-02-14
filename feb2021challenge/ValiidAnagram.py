class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif len(s) == 0:
            return True

        s = sorted(s)
        t = sorted(t)
        for i,ch in enumerate(s):
            if ch != t[i]:
                return False
        return True

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("rat", "car"))
print(sol.isAnagram("", ""))