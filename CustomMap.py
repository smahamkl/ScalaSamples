import types

class Solution:
    def custommap(self, funcs, arr):
        res = map(funcs[0], arr)
        for i in range(1, len(funcs)):
            res = map(funcs[i], res)
        
        return (n for n in list(res))

sol = Solution()
res = sol.custommap([lambda x: x * 2, lambda x: x +2], [1,2,3])
print(type(res))
print(res)
if isinstance(res, types.GeneratorType):
    print("Yes its a generator")