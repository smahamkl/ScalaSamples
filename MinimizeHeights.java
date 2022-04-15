import java.util.Arrays;

/*
LeetCode 910
*/

class MinimizeHeights {
    int getMinDiff(int[] arr, int n, int k) {
        // code here
        Arrays.sort(arr);
        int l = arr.length;
        int ans = arr[l-1] - arr[0];

        for(int i=0;i<l-1;i++)
        {
            int cur = arr[i], next = arr[i+1];
            int high = Math.max(cur+k, arr[l-1]-k);
            int low = Math.min(next-k, arr[0] + k);
            
            ans = Math.min(ans, high-low);
        }

        return ans;

    }

    public static void main(String[] args)
    {
        MinimizeHeights s = new MinimizeHeights();
        System.out.println(s.getMinDiff(new int[]{2,6,3,4,7,2,10,3,2,1}, 10, 5));
    }
}