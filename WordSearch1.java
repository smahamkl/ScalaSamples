import java.util.*;


public class WordSearch1 {

    boolean[][] visited ;

    public boolean dfs(char[][] board, char[] word, int wIdx, int row, int col)
    {
        if(wIdx >= word.length)
            return true;
        
        visited[row][col] = true;
        

        int[][] pmoves = new int[4][2];
        pmoves[0] = new int[]{row-1, col};
        pmoves[1] = new int[]{row+1, col};
        pmoves[2] = new int[]{row, col-1};
        pmoves[3] = new int[]{row, col+1};

        for(int i=0;i<pmoves.length;i++)
        {
           int tmpr = pmoves[i][0];
           int tmpc = pmoves[i][1];
           //System.out.println(tmpr + "," + tmpc);

           if(tmpr >= 0 && tmpr < board.length && tmpc >=0 && tmpc < board[0].length && visited[tmpr][tmpc] == false && word[wIdx] == board[tmpr][tmpc])
           {
               if(dfs(board, word, wIdx+1, tmpr, tmpc))
                return true;
           }
                       
        } 
        visited[row][col] = false;
        return false;     
        
    }
    public boolean exist(char[][] board, String word) {

        int rows = board.length;
        int cols = board[0].length;
        char[] w = word.toCharArray();

       visited = new boolean[rows][cols];

       for(int r = 0;r<rows;r++)
        {
            for(int c = 0;c<cols;c++)
            {
                if(board[r][c] == w[0])
                {
                    //do a DFS search
                    if(dfs(board, w, 1, r, c))
                        return true;
                }
            }
        }
        return false;
        
    }

    public static void main(String[] args)
    {
        WordSearch1 obj = new WordSearch1();

        char[][] board1 = new char[][]{{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        char[][] board = new char[][]{{'C','A', 'A'}, {'A', 'A','A'}, {'B', 'C', 'D'}};

        System.out.println(obj.exist(board, "AAB"));
    }
}
