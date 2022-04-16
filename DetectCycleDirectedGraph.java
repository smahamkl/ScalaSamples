import java.util.*;

public class DetectCycleDirectedGraph {

    public boolean isCyclic(int V, ArrayList<List<Integer>> adj) {
        // code here
        boolean []vis = new boolean[V]; 
        boolean []rStack = new boolean[V];
        
        for(int i=0; i<V; i++){
            if(!vis[i]){
                if(dfs(i,vis,adj,rStack))
                    return true;
            }
        }
        return false;
    }
    boolean dfs(int v,boolean[] vis, ArrayList<List<Integer>> adj,boolean[] rStack){
        vis[v] = true;
        rStack[v] = true;
        for(int i : adj.get(v)){
            if(!vis[i]){
                if(dfs(i,vis,adj,rStack))
                    return true;
            }
            else if(rStack[i])
                return true;
        }
        rStack[v] = false;
        return false;
    }

    public static void main(String[] args)
    {
        DetectCycleDirectedGraph obj = new DetectCycleDirectedGraph();
        ArrayList<List<Integer>> input  = new ArrayList<>();
        input.add(Arrays.asList(new Integer[]{1}));
        input.add(Arrays.asList(new Integer[]{2}));
        input.add(Arrays.asList(new Integer[]{3}));
        input.add(Arrays.asList(new Integer[]{}));

        System.out.println(obj.isCyclic(4, input));
    }
}
