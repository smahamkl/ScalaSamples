from typing import Deque, List
from collections import deque

'''
LeetCode 909
Snakes and Ladders
https://www.youtube.com/watch?v=6lH4nO3JfLk&t=645s
'''
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        length = len(board)
        board.reverse()
        print(length)

        def squareToRowCol(pos:int):
            r = (pos - 1) // length
            c = (pos - 1) % length

            if r % 2:
                c = length - c - 1
            return [r,c]
        
        moves = deque()
        moves.append([1,0])
        visited = set()

        while moves:

            square, level = moves.popleft()
            
            for i in range(1,7):
                nextSquare = square + i
                r,c = squareToRowCol(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                
                if nextSquare == length * length:
                    return level + 1

                if nextSquare not in visited:
                    visited.add(nextSquare)
                    moves.append([nextSquare, level + 1])
                
            
        return -1

sol = Solution()
#print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(sol.snakesAndLadders([[-1,-1],[-1,3]]))