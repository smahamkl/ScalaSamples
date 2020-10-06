from typing import List
from collections import OrderedDict
from collections import Counter
from collections import deque

# class RecentCounter:
#     def __init__(self):
#         self.requests = []
#         self.cur_time = 0

#     def ping(self, t: int) -> int:
#         self.requests.append(t)
#         self.cur_time = t

#         if self.cur_time > 3000:
#             self.requests = [x for x in self.requests if x >= (self.cur_time - 3000)]
#             return len(self.requests)
#         else:
#             return len(self.requests)

class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

        
        
obj = RecentCounter()
for i in range(1, 1000000):
    print(i)
    print(obj.ping(i))