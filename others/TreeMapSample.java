package others;
import java.util.*;

public class TreeMapSample {
    public static void main(String[] args)
    {

        TreeMap<Integer, String> tm = new TreeMap<Integer, String>();
        tm.put(15, "Entry1");
        tm.put(1, "Entry2");
        tm.put(14, "Entry3");
        tm.forEach((k,v)-> System.out.println(k + ":" + v));

        //----PriorityQueue sample
        Queue<String> pq = new PriorityQueue<String>();
        pq.add("Hi");
        pq.add("Geeks"); 
        pq.add("For"); 
        pq.add("Geeks"); 
        System.out.println(pq);
        System.out.println("Poll Method " + pq.poll()); 
        System.out.println("Peek Method " + pq.peek()); 
    }
    
}
