import java.util.*;

/*
Leaders in an array:
Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader 
if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 
*/
public class LeadersOfArray {

    static ArrayList<Integer> leaders(int arr[], int n){
        // Your code here
        Stack<Integer> s = new Stack<>();
        s.push(arr[n-1]);

        for(int i=n-2;i>=0;i--)
        {
            if(arr[i] > s.peek())
                s.push(arr[i]);
        }

        ArrayList<Integer> l = new ArrayList<>();
        while(!s.isEmpty())
            l.add(s.pop());
        
        return l;
    }

    public static void main(String[] args)
    {
        LeadersOfArray obj = new LeadersOfArray();
        List<Integer> ans = obj.leaders(new int[]{1}, 1);

        for(int i:ans)
            System.out.print(i + ",");
    }
    
}
