import java.util.*;

public class PartitionEqualSubsetSum {

    static int dfsBacktrack(int[] arr, int idx, int part[], int partSum)
    {
        if(idx >= arr.length)
            return 1;
        
        for(int i=0;i<=1;i++)
        {
            if(part[i] + arr[idx] <= partSum)
                {
                    part[i] += arr[idx];
                    if(dfsBacktrack(arr, idx+1, part, partSum) == 1)
                        return 1;
                    
                    part[i] -= arr[idx];
                }

        }
        return 0;
        
    }
    
    static int equalPartition(int N, int arr[])
    {
        // code here
        int sum = 0;
        for(int i=0;i<N; i++)
        {
            sum += arr[i];
        }
        if(sum % 2 == 1)
            return 0;

        return dfsBacktrack(arr, 0, new int[]{0,0}, sum/2);
    }

    public static void main(String[] args)
    {
        System.out.println(equalPartition(4, new int[]{1, 5, 11, 5}));
    }
}
