package dec2020challenge;

/*
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
*/
public class MountainArray {

    public boolean validMountainArray(int[] arr) {
        if(arr.length < 3)
            return false;
        
        boolean vpoint = false;

        for(int i=1;i<arr.length;i++)
        {
            if(arr[i] == arr[i-1])
                return false;

            if(!vpoint && arr[i] < arr[i-1])
                vpoint = true;
            
            if(vpoint && (i == 1 || arr[i] >= arr[i-1]))
                return false;
        }

        if(!vpoint)
            return false;
        return true;
    }

    public static void main(String[] args){

        System.out.println(new MountainArray().validMountainArray(new int[]{0,1,2,3,4,5,6,7,8,9}));
        System.out.println(new MountainArray().validMountainArray(new int[]{9,8,7,6,5,4,3,2,1,0}));
        //System.out.println(new MountainArray().validMountainArray(new int[]{0,5,4}));

    }
    
}
