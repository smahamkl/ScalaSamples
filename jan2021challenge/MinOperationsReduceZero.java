package jan2021challenge;

import java.util.HashMap;

class MinOperationsReduceZero{
    public int minOperations(int[] nums, int x) {

        HashMap<Integer, Integer> prefixSum = new HashMap<>();
        HashMap<Integer, Integer> suffixSum = new HashMap<>();
    
        int n = nums.length;
        int leftSum = 0;
        int rightSum = 0;
        for(int i = 0, j = n-1; i < n ; i++, j--) {
            int picked = i + 1;
            prefixSum.put(leftSum + nums[i], picked);
            suffixSum.put(rightSum + nums[j], picked);
    
            leftSum += nums[i];
            rightSum += nums[j];
        }
    
        int minPicks = 100001;
        leftSum = 0;
        rightSum = 0;
        for(int i = 0, j = n-1; i < n ; i++, j--) {
            int picked = i + 1;
            leftSum += nums[i];
            rightSum += nums[j];
    
            if(suffixSum.containsKey(x-leftSum)) 
                minPicks = Math.min(minPicks, picked + suffixSum.get(x-leftSum));
    
            if(prefixSum.containsKey(x-rightSum)) 
                minPicks = Math.min(minPicks, picked + prefixSum.get(x-rightSum));
    
            if(leftSum == x || rightSum == x)
                minPicks = Math.min(minPicks, picked);
        }
    
        return (minPicks > n ? -1 : minPicks);
    }

    public static void main(String[] args){
        System.out.println(new MinOperationsReduceZero().minOperations(new int[]{3,2,20,1,1,3}, 10));
    }
}