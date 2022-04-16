import java.util.*;

public class SnakeLadderProblem {

    static final class Moves{
        public int position;
        public int totalMoves;

        public Moves(int pos, int tm)
        {
            this.position = pos;
            this.totalMoves = tm;
        }
    }

    
    static int minThrow(int N, int arr[]){
        // code here
        Map<Integer, Integer> sl = new HashMap<>();
        boolean[] visited = new boolean[36];

        for(int i=0;i<N;i++)
            sl.put(arr[2*i], arr[2*i+1]);
        
        Deque<Moves> moves = new LinkedList<Moves>();
        if(sl.containsKey(1))
            moves.add(new Moves(sl.get(0), 0));
        else
           moves.addLast(new Moves(1, 0));
          
        while(!moves.isEmpty())
        {
            Moves curMove = moves.pollFirst();

            if(curMove.position >= 30)
                return curMove.totalMoves;

            for(int i=1; i<= 6; i++)
            {
                int tmp = curMove.position + i;
                int totalMoves = curMove.totalMoves + 1;

                if(sl.containsKey(tmp))
                    tmp = sl.get(tmp);
                
                
                if(tmp <= 30 && !visited[tmp])
                {
                    visited[tmp] = true;
                    moves.addLast(new Moves(tmp, totalMoves));
                }
                
            }
        }
        return -1;

    }

    public static void main(String[] args)
    {
        int[] input1 = new int[]{3, 22, 5, 8, 11, 26, 20, 29, 
            17, 4, 19, 7, 27, 1, 21, 9};
        
        int[] input = new int[]{21,8,13,29,16,26};
        
        System.out.println(minThrow(3, input));
    }
    
}
