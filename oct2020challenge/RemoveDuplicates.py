from typing import List
import collections

class Solution:
    #---Method too expensive iterating through the range of numbers--
    # def powerSet(self, set, set_size, sub_len, uniq_ltrs)->str:
    #     power_set_size = 2 ** set_size
    #     tmp1 = "z" * sub_len
    #     for i in range(int("1"*sub_len,2), power_set_size):
    #         tmp = ""
    #         tot = sum([int(x) for x in bin(i)[2:]])
    #         if tot != sub_len:
    #             continue
    #         for j in range(0, set_size):
    #             if i & (1 << j) > 0:
    #                 tmp += set[j]
            
    #         if len(tmp) == sub_len and sorted(tmp) == uniq_ltrs:
    #             tmp1 = min(tmp, tmp1)
    #     return tmp1
    #----working solution------------------
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        print(count)
        stack = []
        added = set()
        for char in s:
            if char not in added:
                while stack and char < stack[-1] and count[stack[-1]] > 0:
                    added.remove(stack.pop())
                stack.append(char)
                added.add(char)
            count[char] -= 1
            print(stack)
        return ''.join(stack)
    #----not working-----------------------
    # def removeDuplicateLetters(self, s: str) -> str:
    #     if len(s) <= 1:
    #         return s

    #     b = {item:count for item, count in collections.Counter(s).items() if count > 1}
    #     a = {x:b[x] for x in sorted(b.keys(), reverse=True)}
    #     if len(a) == 0:
    #         return s
    #     tmp = "z"*26
    #     iterate = True
    #     new_str =s
    #     while iterate:
    #         #a = {item:count for item, count in collections.Counter(new_str).items() if count > 1}
    #         a = {x:a[x] for x in a.keys() if a[x] > 1}
    #         print("duplicates:" + str(a))
    #         if len(a) == 0:
    #             iterate = False
    #             break
    #         for k in a.keys():
    #             while a[k] > 1:
    #                 new_str = new_str.replace(k,'',1)
    #                 a[k] -= 1
    #                 a1 = list(collections.Counter(new_str))
    #                 tmp = min(''.join(a1), tmp)
    #     return tmp
        #return self.powerSet(s, len(s), len(a), a)
        

sol = Solution()
print(sol.removeDuplicateLetters("cbacdcbc"))
b = [1,2,3,4]
print(b[-1])
#print(sol.removeDuplicateLetters("bcabc"))
#print(sol.removeDuplicateLetters("ccacbaba"))
#print(sol.removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz"))