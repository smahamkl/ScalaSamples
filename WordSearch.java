import java.util.*;

public class WordSearch {

    int[][] visited;
    int rowlen;
    int collen;
        
    public boolean isValid(int[] move)
    {
      if(move[0] >= 0 && move[1] >= 0 && move[0] < rowlen && move[1] < collen && visited[move[0]][move[1]] == 0)
        return true;
    
       return false;
    }
    public boolean dfsBacktrack(char[][] board, String word, int row, int col, int idx)
    {
        if(idx >= word.length()-1)
            return true;
        
        int[][] nextMoves = new int[4][2];
        
        nextMoves[0] = new int[]{row-1, col};
        nextMoves[1] = new int[]{row+1, col};
        nextMoves[2] = new int[]{row, col+1};
        nextMoves[3] = new int[]{row, col-1};

        //System.out.println(row + "," + col + "," + idx);

        for(int[] curMove: nextMoves)
        {
            int r = curMove[0];
            int c = curMove[1];
            if(isValid(curMove) && board[r][c] == word.charAt(idx+1)){

                visited[r][c] = 1;
                if(dfsBacktrack(board, word, r, c, idx+1))
                    return true;
                
                visited[r][c] = 0;
            }
        }

        return false;
    }

    public boolean exist(char[][] board, String word) {

        rowlen = board.length;
        collen = board[0].length;
        visited = new int[rowlen][collen];

        if(word.length() > (rowlen * collen))
            return false;

        for(int i=0;i<rowlen;i++)
        {
            for(int j=0;j<collen;j++)
            {
                if(board[i][j] == word.charAt(0)){
                    visited[i][j] = 1;
                    if(dfsBacktrack(board, word, i, j, 0))
                        return true;

                    visited[i][j] = 0;
                }
            }
        }
        return false;
    }

    public static void main(String[] args)
    {
        WordSearch obj = new WordSearch();
        char[][] board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        //char[][] board = {{'A','A'}};
        //char[][] board = {{'A','A','A','A','A','A'},{'A','A','A','A','A','A'},{'A','A','A','A','A','A'},{'A','A','A','A','A','A'},{'A','A','A','A','A','B'},{'A','A','A','A','B','A'}};
        String word = "SEE";
        System.out.println(obj.exist(board, word));
    }
}
