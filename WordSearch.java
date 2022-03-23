import java.util.*;

public class WordSearch {

    int[][] visited;
    int rowlen;
    int collen;

    public boolean isValid(List<Integer> move)
    {
      if(move.get(0) >= 0 && move.get(1) >= 0 && move.get(0) < rowlen && move.get(1) < collen && visited[move.get(0)][move.get(1)] == 0)
        return true;
    
       return false;
    }
    public boolean dfsBacktrack(char[][] board, String word, int row, int col, int idx)
    {
        if(idx >= word.length()-1)
            return true;
        
        List<List<Integer>> nextMoves = new ArrayList<>();
        nextMoves.add(Arrays.asList(new Integer[]{row-1, col}));
        nextMoves.add(Arrays.asList(new Integer[]{row+1, col}));
        nextMoves.add(Arrays.asList(new Integer[]{row, col+1}));
        nextMoves.add(Arrays.asList(new Integer[]{row, col-1}));

        //System.out.println(row + "," + col + "," + idx);

        for(List<Integer> curMove: nextMoves)
        {
            int r = curMove.get(0);
            int c = curMove.get(1);
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
        word = new StringBuilder(word).reverse().toString();

        rowlen = board.length;
        collen = board[0].length;
        visited = new int[rowlen][collen];

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
        //char[][] board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        //char[][] board = {{'A','A'}};
        char[][] board = {{'A','A','A','A','A','A'},{'A','A','A','A','A','A'},{'A','A','A','A','A','A'},{'A','A','A','A','A','A'},{'A','A','A','A','A','B'},{'A','A','A','A','B','A'}};
        String word = "AAAAAAAAAAAAABB";
        System.out.println(obj.exist(board, word));
    }
}
