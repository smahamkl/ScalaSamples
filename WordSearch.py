from typing import List

'''
LeetCode 79. Word Search
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowlen, collen = len(board), len(board[0])
        visited = set()

        def wordsearch_backtrack(row:int, col:int, charPos:int)->bool:
            if charPos >= len(word):
                return True
            print(row, col, charPos)
            
            for i,j in [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]:
                if i >=0 and i < rowlen and j >= 0 and j < collen and board[i][j] == word[charPos] and (i,j) not in visited:
                    visited.add((i, j))
                    if wordsearch_backtrack(i, j, charPos+1):
                        return True
                    visited.remove((i, j))
            return False

        
        for i in range(rowlen):
            for j in range(collen):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if wordsearch_backtrack(i, j, 1):
                        return True
                    else:
                        visited.remove((i, j))
        return False
    


sol = Solution()
#print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
#print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
#print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(sol.exist([["A","A"]], "AAA"))
